import pygame, pgzero, pgzrun
import random


class Game:
    WIDTH = 1920  # window size
    HEIGHT = 1050
    top_left_x = 100
    top_left_y = 150

    DEMO_OBJECTS = [images.black, images.white]

    def __init__(self):
        self.index = 0
        self.old_map = []
        self.Map = []

    def GRM(self):
        # GRM = Generate Random Map

        self.Map = []
        for y in range(28):
            self.Map.append([])
            for x in range(58):
                self.ran = random.randint(0, 1)
                self.Map[len(self.Map) - 1].append(self.ran)

        self.room_height = len(self.Map)
        self.room_width = len(self.Map[0])

    def SM(self):
        # SM = Simulate Map

        self.index += 1

        new_Map = []
        for y in range(self.room_height):
            new_Map.append([])
            for x in range(self.room_width):
                new_Map[len(new_Map) - 1].append(0)

        row = 0
        column = 0
        for y in range(self.room_height):
            for x in range(self.room_width):
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
                        Neighbour_sum = (self.Map[row + 1][column] + self.Map[row + 1][column + 1]) + \
                                        (self.Map[row][column + 1])
                    elif column == (self.room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X ? N
                        #  1 | X X X ? ?
                        #  2 | X X X X X
                        #  3 | X X X X X
                        #  4 | X X X X X
                        Neighbour_sum = (self.Map[row + 1][column - 1] + self.Map[row + 1][column]) + \
                                        (self.Map[row][column - 1])
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | ? N N N ?
                        #  1 | ? ? ? ? ?
                        #  2 | X X X X X
                        #  3 | X X X X X
                        #  4 | X X X X X
                        Neighbour_sum = (self.Map[row + 1][column - 1] + self.Map[row + 1][column] + self.Map[row + 1][
                            column + 1]) + \
                                        (self.Map[row][column - 1] + self.Map[row][column + 1])
                elif row == (self.room_height - 1):
                    if column == 0:
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | ? ? X X X
                        #  4 | N ? X X X
                        Neighbour_sum = (self.Map[row][column + 1]) + \
                                        (self.Map[row - 1][column] + self.Map[row - 1][column + 1])
                    elif column == (self.room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | X X X ? ?
                        #  4 | X X X ? N
                        Neighbour_sum = (self.Map[row][column - 1]) + \
                                        (self.Map[row - 1][column - 1] + self.Map[row - 1][column])
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | X X X X X
                        #  1 | X X X X X
                        #  2 | X X X X X
                        #  3 | ? ? ? ? ?
                        #  4 | ? N N N ?
                        Neighbour_sum = (self.Map[row][column - 1] + self.Map[row][column + 1]) + \
                                        (self.Map[row - 1][column - 1] + self.Map[row - 1][column] + self.Map[row - 1][
                                            column + 1])

                else:
                    if column == 0:
                        # ___|_0_1_2_3_4_
                        #  0 | ? ? X X X
                        #  1 | N ? X X X
                        #  2 | N ? X X X
                        #  3 | N ? X X X
                        #  4 | ? ? X X X
                        Neighbour_sum = (self.Map[row + 1][column] + self.Map[row + 1][column + 1]) + \
                                        (self.Map[row][column + 1]) + \
                                        (self.Map[row - 1][column] + self.Map[row - 1][column + 1])
                    elif column == (self.room_width - 1):
                        # ___|_0_1_2_3_4_
                        #  0 | X X X ? ?
                        #  1 | X X X ? N
                        #  2 | X X X ? N
                        #  3 | X X X ? N
                        #  4 | X X X ? ?
                        Neighbour_sum = (self.Map[row + 1][column - 1] + self.Map[row + 1][column]) + \
                                        (self.Map[row][column - 1]) + \
                                        (self.Map[row - 1][column - 1] + self.Map[row - 1][column])
                    else:
                        # ___|_0_1_2_3_4_
                        #  0 | ? ? ? ? ?
                        #  1 | ? N N N ?
                        #  2 | ? N N N ?
                        #  3 | ? N N N ?
                        #  4 | ? ? ? ? ?
                        Neighbour_sum = (self.Map[row + 1][column - 1] + self.Map[row + 1][column] + self.Map[row + 1][
                            column + 1]) + \
                                        (self.Map[row][column - 1] + self.Map[row][column + 1]) + \
                                        (self.Map[row - 1][column - 1] + self.Map[row - 1][column] + self.Map[row - 1][
                                            column + 1])

                if self.Map[row][column] == 1:
                    if Neighbour_sum > 3 or Neighbour_sum < 2:
                        new_Map[row][column] = 0
                    else:
                        new_Map[row][column] = self.Map[row][column]

                else:
                    if Neighbour_sum == 3:
                        new_Map[row][column] = 1
                    else:
                        new_Map[row][column] = self.Map[row][column]

                column += 1

            row += 1
            column = 0

        self.Map = new_Map

        if self.index >= random.choice([4, 3]):
            if self.Map == self.old_map:
                self.GRM()
            else:
                self.old_map = self.Map
            self.index = 0

    def Start(self):
        global WIDTH, HEIGHT
        WIDTH = self.WIDTH
        HEIGHT = self.HEIGHT
        self.GRM()
        clock.schedule_interval(game.SM, 0.1)

    def Pause(self):
        clock.unschedule(game.SM)


game = Game()
game.Start()


def draw():
    for y in range(game.room_height):
        for x in range(game.room_width):
            image_to_draw = game.DEMO_OBJECTS[0]
            screen.blit(image_to_draw,
                        (game.top_left_x + (x * 30),
                         game.top_left_y + (y * 30) - image_to_draw.get_height()))
            image_to_draw = game.DEMO_OBJECTS[game.Map[y][x]]
            screen.blit(image_to_draw,
                        (game.top_left_x + (x * 30),
                         game.top_left_y + (y * 30) - image_to_draw.get_height()))


pgzrun.go()
