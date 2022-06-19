import pygame, pgzero, pgzrun
import random

### VARIABLES >>>
#################


WIDTH = 1920
HEIGHT = 1050

top_left_x = 135
top_left_y = 150

TILE_SIZE = 30

mouse_pos = [0, 0]
mouse_x = mouse_pos[0]
mouse_y = mouse_pos[1]

simulate = False

room_height = 28
room_width = 58

old_map = []

index = 0



### MAJOR FUNCTIONS >>>
#######################


def on_mouse_down(pos):
    global mouse_pos, mouse_x, mouse_y

    mouse_pos = pos
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]


def simulation():
    global Map, old_map, index, simulate, buttons

    if simulate:
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
                simulate = False
            else:
                old_map = Map
                simulate = True

            index = 0

        buttons = []
        for y in range(len(Map)):
            buttons.append([])
            for x in range(len(Map[0])):
                if Map[y][x] == 0:
                    image = images.black
                else:
                    image = images.white
                buttons[len(buttons) - 1].append(Button((image, x*TILE_SIZE + top_left_x, y*TILE_SIZE + top_left_y), "img"))



### MAJOR CLASSES >>>
#####################


class Button:
    def __init__(self,
                 design, type):
        self.design = design
        self.type = type

        if self.type == "rect":
            self.x = design[0]
            self.y = design[1]
            self.width = design[2]
            self.height = design[3]
            self.fill_colour = design[4]
            self.text = design[5]
            self.text_colour = design[6]

        elif self.type == "img":
            self.image = design[0]
            self.x = design[1]
            self.y = design[2]
            self.width = self.image.get_width()
            self.height = self.image.get_height()


    def draw(self):
        if self.type == "rect":
            draw_rect(self.x, self.y,
                      self.width, self.height,
                      self.fill_colour,
                      None)
            show_text(self.text,
                      (self.x - int(self.width/2), self.y - int(self.height/5), self.width, self.height/2),
                      self.text_colour)
        elif self.type == "img":
            draw_image(self.image, self.x - int(self.width/2), self.y - int(self.height/2))


    def call(self):
        if (self.x - (self.width / 2)) < mouse_x + self.width < (self.x + (self.width / 2)) \
                and (self.y - (self.height / 2)) < mouse_y + self.height < (self.y + (self.height / 2)):
            self.command()



    def command(self):
        if self.image == images.black:
            self.image = images.white
        else:
            self.image = images.black
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw()


class Button2(Button):
    def __init__(self, design, type):
        super().__init__(design, type)

    def command(self):
        global simulate, Map

        if self.image == images.play:
            self.image = images.stop
            simulate = True
            create_map()
        else:
            self.image = images.play
            simulate = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw()


def create_map():
    global Map

    Map = []
    for row in buttons:
        Map.append([])
        for button in row:
            if button.image == images.black:
                Map[len(Map) - 1].append(0)
            else:
                Map[len(Map) - 1].append(1)

    # for y in range(len(Map)):
    #     for x in range(len(Map[0])):
    #         print(Map[y][x], end=" ")
    #     print()


### INITIALIZATIONS >>>
#######################


buttons = []
buttons2 = []
Map = []

for y in range(28):
    Map.append([])
    for x in range(58):
        Map[len(Map) - 1].append(0)

for y in range(28):
    buttons.append([])
    for x in range(58):
        buttons[len(buttons) - 1].append(Button((images.black, x*TILE_SIZE + top_left_x, y*TILE_SIZE + top_left_y), "img")
                       )

buttons2.append(Button2((images.play, 50*TILE_SIZE + top_left_x, -1*TILE_SIZE + top_left_y), "img"))


### BASIC FUNCTIONS >>>
#######################


def draw():
    screen.clear()
    screen.fill("grey")

    for row in buttons:
        for button in row:
            button.draw()
            if simulate is False:
                button.call()

    for button in buttons2:
        button.draw()
        button.call()


def draw_image(image, x, y):
    screen.blit(image,
                (x - image.get_width(),
                 y - image.get_height()))


def draw_rect(x, y,
              width, height,
              colour="white",
              outline=None):
    if outline is not None:
        BOX2 = Rect((x - int(width / 2) - 2, y - int(height / 2) - 2),
                    (width + 4, height + 4)
                    )
        screen.draw.rect(BOX2, outline)

    if colour is not None:
        BOX = Rect((x - int(width / 2), y - int(height / 2)),
                   (width, height)
                   )
        screen.draw.filled_rect(BOX, colour)


def show_text(text_to_show, rect, colour):
    screen.draw.textbox(text_to_show, rect, color=colour)


clock.schedule_interval(simulation, 0.1)

pgzrun.go()