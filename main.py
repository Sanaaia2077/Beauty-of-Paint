from turtle import * 

t = Turtle ()
t.color('black')
t.width(6)
t.shape('circle')
t.speed(4)
t.pendown()

def draw(x,y):
    t.goto(x,y)

t.ondrag(draw)
    
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def set_purple():
    t.color('purple')

def set_blue():
    t.color('blue')

def set_pink():
    t.color('pink')

def set_yellow():
    t.color('yellow')

def set_green():
    t.color('green')

def step_right():
    t.goto(t.xcor()+5,t.ycor())
def step_left():
    t.goto(t.xcor()-5,t.ycor())
def step_up():
    t.goto(t.xcor(),t.ycor()+5)
def step_down():
    t.goto(t.xcor(),t.ycor()-5)

def fill1():
    t.begin_fill()
def fill2():
    t.end_fill()


scr = t.getscreen()
scr.onscreenclick(move)


scr.listen()
scr.onkey(set_purple,'p')
scr.onkey(set_pink,'i')
scr.onkey(set_green,'g')
scr.onkey(set_blue,'b')
scr.onkey(set_yellow,'y')


scr.onkey(step_right,'Right')
scr.onkey(step_left,'Left')
scr.onkey(step_up,'Up')
scr.onkey(step_down,'Down')

scr.onkey(fill1,'f')
scr.onkey(fill2,'l')
