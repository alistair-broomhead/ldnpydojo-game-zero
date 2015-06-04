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
        self._hash_from = object()
        self.x = WIDTH-10
        self.y = random.randint(0, HEIGHT)

    def __hash__(self):
        return hash(self._hash_from)

    def tick(self):
        self.x -= 5
        self.draw()


enemies = {Green()}
projectiles = []


def draw():
    global t

    t += 1

    if t % 50 == 0:
        enemies.add(Green())

    screen.clear()

    to_remove = set()

    for enemy in enemies:
        enemy.tick()

        if enemy.x < 10:
            to_remove.add(enemy)

    for enemy in to_remove:
        enemies.remove(enemy)

    to_remove = []

    for i, projectile in enumerate(projectiles):
        projectile.x += 10
        if projectile.x > WIDTH:
            to_remove.append(i)
        projectile.draw()

    for i in reversed(to_remove):
        del projectiles[i]

    player.draw()

def update():
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



