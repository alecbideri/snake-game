from turtle import Turtle
starting_positions = [(0,0) ,(-20 ,0) ,(-40 ,0)]
MOVE_DISTANCE = 20
up = 90
down = 270
left = 180
right = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self , position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(up)
    def down(self):
        if self.segments[0].heading() != up:
          self.segments[0].setheading(down)
    def right(self):
        if self.segments[0].heading() != left:
          self.segments[0].setheading(right)
    def left(self):
        if self.segments[0].heading() != right:
           self.segments[0].setheading(left)