import pygame, pgzero, pgzrun
import time

Map = [[0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

WIDTH = 800  # window size
HEIGHT = 800
top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.black, images.white]

room_height = 5
room_width = 5


def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[Map[y][x]]
            screen.blit(image_to_draw,
                        (top_left_x + (x * 30),
                         top_left_y + (y * 30) - image_to_draw.get_height()))


def change_map():
    global Map
    new_Map = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    row = 0
    column = 0
    if keyboard.right:
        for y in range(room_height):
            for x in range(room_width):
                # ___|_0_1_2_3_4_
                #  0 | 0 0 0 0 0
                #  1 | 1 1 1 1 0
                #  2 | 0 0 1 1 0
                #  3 | 0 0 0 1 0
                #  4 | 0 0 0 0 0

                # [y + 1][x - 1] [y + 1][x] [y + 1][x + 1]
                #   [y][x - 1]     [y][x]     [y][x + 1]
                # [y - 1][x - 1] [y - 1][x] [y - 1][x + 1]

                # print(Map[row + 2][column + 3])

                # Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1])  # <<< Code, Concept >>> # [y + 1][x - 1] [y + 1][x] [y + 1][x + 1]
                # Neighbour_sum += (Map[row][column - 1] + Map[row][column] + Map[row][column + 1])             # <<< Code, Concept >>> #   [y][x - 1]     [y][x]     [y][x + 1]
                # Neighbour_sum += (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1]) # <<< Code, Concept >>> # [y - 1][x - 1] [y - 1][x] [y - 1][x + 1]

                if row == 0:
                    if column == 0:
                        # ___|_0_1_2_3_4_
                        #  0 | N ? X X X
                        #  1 | ? ? X X X
                        #  2 | X X X X X
                        #  3 | X X X X X
                        #  4 | X X X X X
                        Neighbour_sum = (Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                        (Map[row][column + 1])
                        # Checked

                    elif column == (room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X ? N
                        #  1 | X X X ? ?
                        #  2 | X X X X X
                        #  3 | X X X X X
                        #  4 | X X X X X
                        Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column]) + \
                                        (Map[row][column - 1])
                        # Checked
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | ? N N N ?
                        #  1 | ? ? ? ? ?
                        #  2 | X X X X X
                        #  3 | X X X X X
                        #  4 | X X X X X
                        Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                        (Map[row][column - 1] + Map[row][column + 1])
                        # Checked

                elif row == (room_height - 1):
                    if column == 0:
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | ? ? X X X
                        #  4 | N ? X X X
                        Neighbour_sum = (Map[row][column + 1]) + \
                                        (Map[row - 1][column] + Map[row - 1][column + 1])
                        # Checked
                    elif column == (room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | X X X ? ?
                        #  4 | X X X ? N
                        Neighbour_sum = (Map[row][column - 1]) + \
                                        (Map[row - 1][column - 1] + Map[row - 1][column])
                        # Checked
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | ? ? ? ? ?
                        #  4 | ? N N N ?
                        Neighbour_sum = (Map[row][column - 1] + Map[row][column + 1]) + \
                                        (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1])
                        # Checked

                else:
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    if column == 0:
                        # ___|_0_1_2_3_4_
                        #  0 | ? ? X X X
                        #  1 | N ? X X X
                        #  2 | N ? X X X
                        #  3 | N ? X X X
                        #  4 | ? ? X X X
                        Neighbour_sum = (Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                        (Map[row][column + 1]) + \
                                        (Map[row - 1][column] + Map[row - 1][column + 1])
                        # Checked
                    elif column == (room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X ? ?
                        #  1 | X X X ? N
                        #  2 | X X X ? N
                        #  3 | X X X ? N
                        #  4 | X X X ? ?
                        Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column]) + \
                                        (Map[row][column - 1]) + \
                                        (Map[row - 1][column - 1] + Map[row - 1][column])
                        # Checked
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | ? ? ? ? ?
                        #  1 | ? N N N ?
                        #  2 | ? N N N ?
                        #  3 | ? N N N ?
                        #  4 | ? ? ? ? ?
                        Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                        (Map[row][column - 1] + Map[row][column + 1]) + \
                                        (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1])
                        # Checked

                if Map[row][column] == 1:
                    if Neighbour_sum > 3 or Neighbour_sum < 2:
                        new_Map[row][column] = 0
                    else:
                        new_Map[row][column] = Map[row][column]

                else:
                    if Neighbour_sum == 3:
                        new_Map[row][column] = 1
                    else:
                        new_Map[row][column] = Map[row][column]

                print(new_Map, "\n", Map)
                print(row, column, Map[row][column], Neighbour_sum, new_Map[row][column])

                column += 1

            row += 1
            column = 0

        Map = new_Map

clock.schedule_interval(change_map, 0.1)

pgzrun.go()
