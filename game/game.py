import pygame
from pygame.locals import *
from sys import exit

from buttons import Pixel_Button, Exit_Button, create_buttons
from simulator import create_map, simulation

my_dir = "/Users/zestra/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/Buttons/game-of-life/images/"

WIDTH = 1920
HEIGHT = 1050

top_left_x = 135
top_left_y = 150

TILE_SIZE = 30

old_map = []

index = 0


pygame.init()

my_screen = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)

buttons = []
for y in range(28):
    buttons.append([])
    for x in range(58):
        buttons[len(buttons) - 1].append(Pixel_Button(0, ["black.png", "white.png"], x*TILE_SIZE + top_left_x, y*TILE_SIZE + top_left_y, pygame.mouse, my_screen))
exit_button = Exit_Button("simulate.png", WIDTH - 120, 80, pygame.mouse, my_screen)

Map = create_map(buttons)

simulate = False
play = True
while play:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:

            exit = exit_button.call()
            if exit is True and simulate is True:
                pygame.quit()
                play = False
                break
            elif exit is True and simulate is False:
                simulate = True
                exit_button.img = pygame.image.load(my_dir + "exit.png").convert()

            if simulate is False:
                for y in range(len(buttons) - 1):
                    for x in range(len(buttons[0]) - 1):
                        buttons[y][x].call()
            else:
                Map = create_map(buttons)
                Map = simulation(Map)
                buttons = create_buttons(Map, pygame.mouse, my_screen)


        my_screen.fill("dark grey")

        for y in range(len(buttons) - 1):
            for x in range(len(buttons[0]) - 1):
                buttons[y][x].draw()
        exit_button.draw()

        pygame.display.update()