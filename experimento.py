import pygame, pgzero, pgzrun


def on_mouse_down(pos):
    if pos[0] > 400:
        print("left!")
    else:
        print("right!")


def draw_rect(x, y,
              width, height,
              colour="white"):
    BOX = Rect((x - int(width / 2), y - int(height / 2)),
               (width, height)
               )
    screen.draw.filled_rect(BOX, colour)


def show_text(text_to_show, x, y,
              colour="white",
              size=75):
    screen.draw.text(text_to_show,
                     (x, y),
                     fontsize=size, color=colour)


def draw():
    screen.fill((0, 128, 0))

    draw_rect(400, 0, 5, 10000)

    show_text("right", 150, 25)

    show_text("left", 550, 25)





pgzrun.go()