class Drop:
    def __init__(self):
        self.x = random(630)
        self.y = random(-200,-50)
        self.yspeed = random(4,10)
        self.lon = random(10,20)
    
    def fall(self):
        self.y = self.y + self.yspeed
        self.yspeed = self.yspeed + 0.05
        if(self.y > 360):
            self.y = random(-200,-50)
            self.yspeed = random(4,10)
        
    def show(self):
        stroke(138, 43, 226)
        line(self.x,self.y,self.x,self.y+self.lon)
        
