# Purple Rain
# (138, 43, 226)
# (230, 230, 250) // Background
import Drop as D

d = []

def setup():
    size(640,360)
    for i in range(500):
        d.append(D.Drop())  
    print(len(d))
    
    
def draw():
    background(230, 230, 250)
    print(len(d))
    for i in range(500):
        d[i].fall()
        d[i].show()
