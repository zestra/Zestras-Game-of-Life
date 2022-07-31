import pygame
from pygame.locals import *

my_dir = "/Users/zestra/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/Buttons/game-of-life/images/"


class Pixel_Button:
    def __init__(self, code, imgs, x, y, my_mouse, my_screen):
        self.code = code

        self.imgs = imgs
        self.img = pygame.image.load(my_dir + self.imgs[self.code]).convert()

        self.x = x - self.img.get_width()/2
        self.y = y - self.img.get_height()/2

        self.my_mouse = my_mouse
        self.my_screen = my_screen

    def call(self):
        my_mouse_x, my_mouse_y = self.my_mouse.get_pos()

        if (self.x - (self.img.get_width() / 2) + 7 < my_mouse_x < self.x + (self.img.get_width()) - 7)  \
                and (self.y - (self.img.get_height() / 2) + 7 < my_mouse_y < self.y + self.img.get_height() - 7):
            self.go()

    def draw(self):
        # This draws the button onto the screen.
        self.my_screen.blit(self.img, (self.x, self.y))

    def go(self):
        if self.code == 0:
            self.code = 1
        else:
            self.code = 0

        self.img = pygame.image.load(my_dir + self.imgs[self.code]).convert()


class Exit_Button:
    def __init__(self, img, x, y, my_mouse, my_screen):
        self.img = pygame.image.load(my_dir + img).convert()

        self.x = x - self.img.get_width()/2
        self.y = y - self.img.get_height()/2

        self.my_mouse = my_mouse
        self.my_screen = my_screen

    def call(self):
        my_mouse_x, my_mouse_y = self.my_mouse.get_pos()

        if (self.x - (self.img.get_width() / 2) + 7 < my_mouse_x < self.x + (self.img.get_width()) - 7)  \
                and (self.y - (self.img.get_height() / 2) + 7 < my_mouse_y < self.y + self.img.get_height() - 7):
            return True

    def draw(self):
        # This draws the button onto the screen.
        self.my_screen.blit(self.img, (self.x, self.y))


def create_buttons(Map, my_mouse, my_screen):
    TILE_SIZE = 30
    top_left_x = 135
    top_left_y = 150

    buttons = []
    for y in range(28):
        buttons.append([])
        for x in range(58):
            if Map[y][x] == 0:
                num = 0
            else:
                num = 1
            buttons[len(buttons) - 1].append(Pixel_Button(num, ["black.png", "white.png"], x*TILE_SIZE + top_left_x, y*TILE_SIZE + top_left_y, my_mouse, my_screen))
    return buttons