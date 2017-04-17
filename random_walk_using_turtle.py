import turtle
wn=turtle.Screen()
Philip=turtle.Turtle()

import random

possible_direction = ['N' , 'E' , 'S' , 'W']


def random_walk(number_of_steps,stride):
    for e in range(1,number_of_steps + 1):
        direction = random.choice(possible_direction)
        if direction == 'N':
            Philip.setheading(90)
            Philip.forward(stride)
        if direction == 'E':
            Philip.setheading(0)
            Philip.forward(stride)
        if direction == 'S':
            Philip.setheading(270)
            Philip.forward(stride)
        if direction == 'W':
            Philip.setheading(180)
            Philip.forward(stride)
    return Philip.position()

print (random_walk(1000,1))
