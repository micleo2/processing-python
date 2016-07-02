class Circle:
    def __init__(self, x, y, r=8):
        self.loc = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.radius = r
        
    def draw(self):
        fill(0)
        ellipse(self.loc.x, self.loc.y, self.radius*2, self.radius*2)
        
    def update(self):
        self.velocity.mult(0.99)
        self.velocity.add(self.acceleration)
        self.loc.add(self.velocity)
        self.acceleration.mult(0)

class Enemy(Circle):
    def draw(self):
        fill(255, 0, 0)
        ellipse(self.loc.x, self.loc.y, self.radius*2, self.radius*2)
        
    def update(self, target):
        Circle.update(self)
        if self.loc.x > target.loc.x:
            self.acceleration.x = -0.1
        else:
            self.acceleration.x = 0.1
        
        if self.loc.y > target.loc.y:
            self.acceleration.y = -0.1
        else:
            self.acceleration.y = 0.1
        
class Player(Circle):
    def update(self, keyMap):
        speed = 0.1
        Circle.update(self)
        if keyMap.__contains__(UP) and keyMap[UP]:
            self.acceleration.y = -speed
        elif keyMap.__contains__(DOWN) and keyMap[DOWN]:
            self.acceleration.y = speed
        if keyMap.__contains__(LEFT) and keyMap[LEFT]:
            self.acceleration.x = -speed
        elif keyMap.__contains__(RIGHT) and keyMap[RIGHT]:
            self.acceleration.x = speed