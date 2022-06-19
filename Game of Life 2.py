import pygame, pgzero, pgzrun
import random

index = 0


def GRM():
    # GRM = Generate Random Map

    global Map, room_height, room_width

    Map = []
    for y in range(28):
        Map.append([])
        for x in range(58):
            ran = random.randint(0, 1)
            Map[len(Map) - 1].append(ran)

    room_height = len(Map)
    room_width = len(Map[0])


WIDTH = 1920  # window size
HEIGHT = 1050
top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.black, images.white]

old_map = []


def SM():
    # SM = Simulate Map

    global Map, old_map, index

    index += 1

    new_Map = []
    for y in range(room_height):
        new_Map.append([])
        for x in range(room_width):
            new_Map[len(new_Map) - 1].append(0)

    row = 0
    column = 0
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
                elif column == (room_width - 1):
                    # ___|_0_1_2_3_4_
                    #  0 | X X X ? N
                    #  1 | X X X ? ?
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column]) + \
                                    (Map[row][column - 1])
                else:
                    # ___|_0_1_2_3_4_
                    #  0 | ? N N N ?
                    #  1 | ? ? ? ? ?
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                    (Map[row][column - 1] + Map[row][column + 1])
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
                elif column == (room_width - 1):
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | X X X ? ?
                    #  4 | X X X ? N
                    Neighbour_sum = (Map[row][column - 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column])
                else:
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | ? ? ? ? ?
                    #  4 | ? N N N ?
                    Neighbour_sum = (Map[row][column - 1] + Map[row][column + 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1])

            else:
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

            column += 1

        row += 1
        column = 0

    Map = new_Map

    if index >= random.choice([4, 3]):
        if Map == old_map:
            GRM()
        else:
            old_map = Map
        index = 0


def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[0]
            screen.blit(image_to_draw,
                        (top_left_x + (x * 30),
                         top_left_y + (y * 30) - image_to_draw.get_height()))
            image_to_draw = DEMO_OBJECTS[Map[y][x]]
            screen.blit(image_to_draw,
                        (top_left_x + (x * 30),
                         top_left_y + (y * 30) - image_to_draw.get_height()))


GRM()

clock.schedule_interval(SM, 0.1)

pgzrun.go()
