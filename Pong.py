from pygame import *
from random import randint
font.init()

# region window
WIDTH, HEIGHT = 1000, 725
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
# endregion window

# region Classes
class ImageSprite(sprite.Sprite):
    # constructor function. Runs ONCE every time a new object it's created
    def __init__(self, filename, pos, size):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, size)
        self.rect = Rect(pos, size)
        self.initial_pos = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def reset(self):
        self.rect.topleft = self.initial_pos

class PlayerSprite(ImageSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += 7
        if keys[K_w]:
            self.rect.y -= 7

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def update2(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += 7
        if keys[K_UP]:
            self.rect.y -= 7

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class BallSprite(ImageSprite):
    def __init__(self, filename, pos, size, speed):
        super().__init__(filename, pos, size)
        self.speed = Vector2(speed)
    
    def update(self):
        self.rect.topleft += self.speed
    
    def VerticalBounce(self):
        self.speed.y *= -1
    
    def HorizontalBounce(self):
        self.speed.x *= -1

    def collision(self, other_sprite):
        col = sprite.collide_rect(self,other_sprite)
        return col
        

# region Sprite
p1 = PlayerSprite(filename="VengefulSpirit.png", pos=(0,250), size=(115,70))
p2 = PlayerSprite(filename="ShadeSoul.png", pos=(WIDTH-115,250), size=(115,70))
ball = BallSprite(filename="Dreamball.png", pos=(300,350), size=(70,70), speed=(2,4))
winp1 = ImageSprite(filename="BaldurShell.png", pos=(450,312), size=(100,100))
winp2 = ImageSprite(filename="GrubberflyElegy.png", pos=(450,312), size=(100,100))

while not event.peek(QUIT):
    window.fill("black")
    
    p1.draw(window)
    p1.update1()
    p2.draw(window)
    p2.update2()
    
    if ball.rect.top < 0 or ball.rect.bottom > HEIGHT:
        ball.VerticalBounce()

    if ball.collision(p1):
        ball.HorizontalBounce()
        ball.rect.left = p1.rect.right

    if ball.collision(p2):
        ball.HorizontalBounce()
        ball.rect.right = p2.rect.left

    if ball.rect.left < 0:
        winp1.draw(window)

    if ball.rect.right > WIDTH:
        winp2.draw(window)

    ball.draw(window)
    ball.update()

    display.update()
    clock.tick(100)
