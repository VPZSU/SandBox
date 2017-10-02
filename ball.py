import tkinter

#constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
ZERO = 0
MAIN_BALL_RADIUS = 30
MAIN_BALL_COLOR = 'blue'
INIT_DX = 1
INIT_DY = 1


# balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                           self.y + self.r, fill=self.color)


    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                           self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)

    def move(self):
        # colliding with walls
        if(self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = - self.dx
        if(self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = - self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


# main loop
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(10, main)

#mouse events
def mouse_click(event):
    global main_ball
    #print(event.num, event.x, event.y)
    if event.num == 1:
        main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR,
                           INIT_DX, INIT_DY)
        main_ball.draw()
    else:
        main_ball.hide()


root = tkinter.Tk()
root.title("Colliding Balls")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
main()
root.mainloop()
