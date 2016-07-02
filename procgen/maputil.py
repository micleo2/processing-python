import random

class Tile:
    def __init__(self, s, x, y, w, h):
        self.state = s
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.fillColor = color(0, 0, 0)
        
def createmap(columns, rows, tileWidth, tileHeight):
    cells = []
    for x in range(columns):
        cells.append([])
        for y in range(rows):
            cells[x].append(Tile(1, x, y, tileWidth, tileHeight))
    return cells

def randcoord(map):
    x = random.randrange(0, len(map))
    y = random.randrange(0, len(map[0]))
    return tuple([x, y])

def getunchartedcoord(map):
    x, y = randcoord(map)
    while map[x][y].state == 0:
        x, y = randcoord(map)
    return tuple([x, y])

def shakecoord(x, y, map):
    if random.random() > 0.5:
        x += random.choice([-1, 1])
        x %= len(map)
    else:
        y += random.choice([-1, 1])
        y %= len(map[0])
    return tuple([x, y])