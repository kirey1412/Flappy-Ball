import pgzrun
TITLE="Gravity Ball"
WIDTH=640
HEIGHT=595
gravity=500 #pixel per second
class Ball():
    def __init__(self, x,y, vx, vy, clr, r):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.clr=clr
        self.r=r
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.r, self.clr)
ball1=Ball(300,50,100,0,"pink",50)
    
def draw():
    screen.clear()
    ball1.draw()
def update(dt):
    initialyvelocity=ball1.vy
    print(ball1.y)
    ball1.vy+=gravity*dt
    ball1.y+=(initialyvelocity+ball1.vy)*0.5*dt
    if ball1.y > HEIGHT-ball1.r:
        ball1.y=HEIGHT-ball1.r
        ball1.vy=-ball1.vy*0.9

pgzrun.go()