import turtle

t = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("blue")
t.speed(0)


class Box():
    def __init__(self):
        self.side = 100
        self.color = "yellow"
       
    def draw( self, heading ):
        t.setheading( heading )
        t.color(self.color)
        i = 0
        while (i <= 3):
            t.forward(self.side)
            t.left(90)
            i += 1



class CircleBox():
    def __init__(self):
        self.b = Box()
        

    def fill(self):        
        for l in range(0, 360, 2):
            if l % 3 == 0:
                self.b.color = "white"
            else:
                self.b.color = "yellow"
            self.b.draw(l)
    
       

sun = CircleBox().fill()

win.exitonclick()





