from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

tut = Turtle()
tut.color("black")
tut.penup()
tut.goto(0, -20)
tut.hideturtle()



class Result(Turtle):
    def __init__(self, res, col):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 20)
        self.hideturtle()
        self.wrt(res, col)

    def wrt(self, res, col):
        if res is True:
            self.write(f"You WIN!!!", align=ALIGNMENT, font=FONT)
            tut.write(f"The Winner is {col} Turtle", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"You loose :( better luck next time!", align=ALIGNMENT, font=FONT)
            tut.write(f"The Winner is {col} Turtle", align=ALIGNMENT, font=FONT)

