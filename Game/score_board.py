from turtle import Turtle
align = "center"
font = ("Courier" , 12 , "normal")
class score(Turtle):
    def __init__(self):
        super().__init__()

        # Initialize count
        self.count = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.count}", align=align, font=font)

    def stop_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align=align, font=font)
    def increase_score(self):
        self.count += 1
        self.clear()
        self.update_board()
