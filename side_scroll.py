import random

TITLE = "Super Alien Peril"
HEIGHT = 600
WIDTH = 800

player = Actor('ship')
player.topleft = 10, HEIGHT/2

t = 0

class Green(Actor):

    def __init__(self, img='happy_green_guy'):
        super().__init__(img)
        self.x = WIDTH-10
        self.y = random.randint(0, HEIGHT)

    def tick(self):
        i = self.collidelist(projectiles)
        if i != -1:
            enemies.remove(self)
            del projectiles[i]
        self.x -= 5


enemies = []
projectiles = []


def draw():
    screen.clear()

    for enemy in enemies:
        enemy.draw()

    for projectile in projectiles:
        projectile.draw()

    player.draw()

def update():
    global t

    if t % 50 == 0:
        enemies.append(Green())

    t += 1

    for enemy in enemies.copy():
        enemy.tick()
        if enemy.right < 0:
            enemies.remove(enemy)


    for projectile in projectiles.copy():
        projectile.x += 10
        if projectile.left > WIDTH:
            projectiles.remove(projectile)

    if keyboard.w:
        player.y -= 20
    elif keyboard.s:
        player.y += 20

    if player.y < 0:
        player.y = 0
    elif player.y > HEIGHT:
        player.y = HEIGHT

def on_key_down(key):
    
    if key == keys.SPACE:
        projectile = Actor('evil_blob')
        projectile.x = 20
        projectile.y = player.y
        projectiles.append(projectile)



