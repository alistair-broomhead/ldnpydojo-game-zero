HEIGHT = 600
WIDTH = 800

player = Actor('ship')
player.topleft = 10, HEIGHT/2

def draw():
    screen.clear()
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
