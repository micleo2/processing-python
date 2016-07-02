import Circle
width = 700
height = 700
enemies = []
player = Circle.Player(width/2, height/2)
keyMap = {} #KEY = KEYCODE, VALUE = STATE OF PRESSED
enemies.append(Circle.Enemy(0, 0))
enemies.append(Circle.Enemy(width-1, 0))
enemies.append(Circle.Enemy(0, height-3))
enemies.append(Circle.Enemy(width, height+2))

def setup():
    size(width, height)

def keyPressed(event):
    code = event.keyCode
    keyMap[code] = True
    
def keyReleased(event):
    code = event.keyCode
    keyMap[code] = False
    
def draw():
    background(255, 255, 255)
    for e in enemies:
        e.draw()
        e.update(player)

    player.draw()
    player.update(keyMap)