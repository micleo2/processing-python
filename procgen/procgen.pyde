import maputil
import random
import mapcarver

width = 650
height = 650

def setup():
    size(width, height)

rows = 60
cols = 60
tileWidth = height / cols
tileHeight = width / rows

mainmap = maputil.createmap(cols, rows, tileWidth, tileHeight)
mapcarver.jumpwhencornered(mainmap, 100)

def draw():
    background(255)
    for x in range(cols):
        for y in range(rows):
            currentTile = mainmap[x][y]
            if currentTile.state == 1: #wall
                noStroke()
                fill(155, 155, 155)
                rect(currentTile.x * tileWidth, currentTile.y * tileHeight, currentTile.width, currentTile.height)
            elif currentTile.state == 0: #path
                noStroke()
                fill(currentTile.fillColor)
                rect(currentTile.x * tileWidth, currentTile.y * tileHeight, currentTile.width, currentTile.height)
                