import random
import maputil

def createrandomwalk(map, iterations):
    x, y = maputil.randcoord(map)
    for i in range(iterations):
        x, y = maputil.shakecoord(x, y, map)
        map[x][y].state = 0
        
def jumpwhencornered(map, iterations):
    tracked = []
    x, y = maputil.randcoord(map)
    colorGrad = 255
    for i in range(iterations):
        newcoord = maputil.shakecoord(x, y, map)
        n = 0
        while newcoord in tracked:
            n += 1
            if n >= 8:
                print("JUMPNIG...")
                newcoord = maputil.getunchartedcoord(map)
                break
            newcoord = maputil.shakecoord(x, y, map)
        #now we have an uncharted coordinate!
        x, y = newcoord #decomposition of tuple
        tracked.append(newcoord)
        map[x][y].state = 0
        map[x][y].fillColor = color(colorGrad, 0, 0)
        colorGrad -= 255 / iterations


def dontbacktrack(map, iterations): #high 'failure' rate
    tracked = []
    x, y = maputil.randcoord(map)
    colorGrad = 255
    for i in range(iterations):
        newcoord = maputil.shakecoord(x, y, map)
        n = 0
        while newcoord in tracked:
            n += 1
            if n >= 8:
                print("impossible! got stuck :(")
                return
            newcoord = maputil.shakecoord(x, y, map)
        #now we have an uncharted coordinate!
        x, y = newcoord #decomposition of tuple
        tracked.append(newcoord)
        map[x][y].state = 0
        map[x][y].fillColor = color(colorGrad, 0, 0)
        colorGrad -= 255 / iterations