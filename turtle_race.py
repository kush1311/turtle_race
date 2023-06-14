import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False

screen.setup(1000, 600)
y_positions = [-190, -90, 0, 90, 190, 290]
all_turtles = []

colors = ["red", "black", "yellow", "green", "blue", "purple"]

name = ['ravi', 'dharmil', 'bhavik', 'kushal', 'dhruv', 'harsh']

list_name = dict(zip(colors, name))



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-490, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user = screen.textinput("Make a bet", "Who will win the match ? (red=ravi , blue= dhruv , yellow=bhavik , green=kushal , black=dharmil , purple = harsh)")

if user:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 490:
            is_race_on = False
            winning_color = turtle.color()[0]
            if winning_color == user:
                winning_name = list_name[winning_color]
                print(f"You've won! The {winning_name} turtle is the winner!")
            else:
                winning_name = list_name[winning_color]
                print(f"You've lost! The {winning_name} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
