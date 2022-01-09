from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED = 0
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for eachsegment in STARTING_POS:
            self.add_snake(eachsegment)

    def add_snake(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.speed(SPEED)
        segment.goto(position)
        self.segments.append(segment)


    def extend(self):
        self.add_snake(self.segments[-1].pos())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            seg_pos = self.segments[seg - 1].pos()
            self.segments[seg].goto(seg_pos)
        self.head.forward(MOVE_DISTANCE)


    def reset_game(self):
        self.create_snake()
        self.head = self.segments[0]


    def moveup(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def movedowm(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def moveleft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moveright(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

