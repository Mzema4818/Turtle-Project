def polygon( t ,side, distance):
    angle = 360 / side
    t.begin_fill()
    for times in range(side):
        t.width(25)
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("blue")
    polygon(t,5,100)
    t.color("black")
    polygon(t,4,100)
    t.color("orange")
    polygon(t,3,100)

def design1(t):
    for times in range(225):
        c = (times,times,255)
        print(c)
        t.color(c)
        polygon(t,3,50)
        t.left(45)
        t.penup()
        t.forward(times)
        t.pendown()

def design2(t):
    for times in range(80):
        c = (times,times,255)
        print(c)
        t.color(c)
        polygon(t,3,50)
        t.left(45)
        t.penup()
        t.forward(times)
        t.pendown()

def design3(t):
    for times in range(29):
        c = (times,times,255)
        print(c)
        t.color(c)
        t.forward(100)
        t.left(90)
        t.forward(10+2)
        t.left(50)
        t.forward(7*4)
        t.left(90)
        t.circle(45)

def design4(t):
    for times in range(10):
        c=(times*25,times*15,255)
        print(c)
        t.begin_fill()
        t.color(c)
        t.forward(100)
        t.width(10)
        t.circle(10*2)
        t.left(45)
        t.end_fill()

def design5(t):
    for times in range(10):
        c=(times*25,times*15,255)
        print(c)
        t.begin_fill()
        t.color(c)
        t.forward(90)
        t.width(10)
        t.circle(9*2)
        t.left(45)
        t.end_fill()

def design6(t):
    for times in range(110):
        c = (times,times,255)
        print(c)
        t.color(c)
        polygon(t,3,50)
        t.left(45)
        t.penup()
        t.forward(times)
        t.pendown()        
        
def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def polygons( t ,side, distance):
    angle = 360 / side
    for times in range(side):
        t.width(5)
        t.forward(distance)
        t.left(angle)
    
def design7(t):
    for times in range(256):
        c = (times,times,255)
        print(c)
        t.color(c)
        polygons(t,6,10)
        t.forward(times+10)
        t.left(45)

def design8(t):
    for times in range(256):
        t.goto(0,0)
        t.forward(600)
        t.pendown()
        c = (times,times,255)
        print(c)
        t.color(c)
        polygons(t,6,10)
        t.forward(times+10)
        t.left(45)
