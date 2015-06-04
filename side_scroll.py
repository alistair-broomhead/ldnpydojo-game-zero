HEIGHT = 600
WIDTH = 800

player = Actor('ship')
player.topleft = 10, HEIGHT/2


class Green(Actor):
    def __init__(self, img='happy_green_guy'):
        super().__init__(img)
        self.topright = WIDTH-10, HEIGHT/2

    def tick(self):
        self.x -= 2
        self.draw()


enemies = [Green()]



def draw():
    screen.clear()
    for enemy in enemies:
        enemy.tick()
        
    player.draw()

def update():
    if keyboard.w :
        player.y -= 20
    elif keyboard.s:
        player.y += 20

    if player.y < 0:
        player.y = 0
    elif player.y > HEIGHT:
        player.y = HEIGHT





