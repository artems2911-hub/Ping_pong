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
        self.speed_y = self.speed
        self.speed_x = self.speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 50:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 360:
            self.rect.y += self.speed
    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 50:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 360:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if sprite.collide_rect(ball, rocket_l):
            self.speed_x *= -1
        if sprite.collide_rect(ball, rocket_r):
            self.speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        
            

rocket_l = Player("baseball-bat_pic.png", 30, 130, 10, 40, 20)
rocket_r = Player("baseball-bat_pic.png", 30, 130, 660, 40, 20)
ball = Ball("Dog-ball.png", 50, 50, 400, 200, 5)

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


        rocket_l.update_l()
        rocket_r.update_r()
        ball.update()
        rocket_l.reset()
        rocket_r.reset()
        ball.reset()

        
    display.update()
    clock.tick(FPS)
