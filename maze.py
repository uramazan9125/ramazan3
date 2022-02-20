from pygame import *
 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def Update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5 :
            self.rect.y -= 5
        if keys_pressed[K_DOWN]and self.rect.y <600:
            self.rect.y+= 5
        if keys_pressed[K_LEFT]and self.rect.x >5:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT]and self.rect.x <800:
            self.rect.x += 5
class Enemy(GameSprite):
    direction = 1
    def Update(self):
        # 0 = Право, 1 = Лево
        print(self.rect.x)
        if self.direction == 1:
            self.rect.x -= 5
        if direction == 0:
            self.rect.x += 5
        if self.rect.x <= 620:
            direction = 0
        if self.rect.x >= 820:
            direction = 1

class Wall(sprite.Sprite):
    def __init__(self, color_1,.. wall_x,.. wall_width,..):
        super (). __init__()
        self.color_1 = color_1 #color_2 и color_3 аналогично
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self,image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y 
    def draw_wall(self)

win_width = 900
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = Player('hero.png', 5, win_height - 80, 4)
cyborg = Enemy('cyborg.png', win_width - 80, 500, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

 w1 =Wall(154, 205, 50, 100, 20, 450, 10)
 w2 =Wall(154, 205, 50, 100, 20, 450, 10)
 w3 =Wall(154, 205, 50, 100, 20, 450, 10)
 
game = True
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg') 

font.init()
font = font.font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True,(180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True
        #..
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) ... :
             finish = True
             kick.play()

    player.Update()
    cyborg.Update()

    window.blit(background,(0, 0))
    player.reset()
    cyborg.reset()
 
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) ... :
             finish = True
             window.blit(lose,(200, 200))
             kick.play()





    display.update()
     clock.tick(FPS)

