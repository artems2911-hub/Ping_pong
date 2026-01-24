from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг понг")
background = transform.scale(image.load("background_pic.jpg"), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, image_x, image_y, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_x, image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressef[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed
    
    def update_r(self):
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed

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
