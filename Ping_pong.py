from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг понг")
background = transform.scale(image.load("background_pic.jpg"), (win_width, win_height))

clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))

        
    display.update()
    clock.tick(FPS)