
###TURTLE RACE###
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup (width = 700, height = 600)
user_bet = screen.textinput (title = "Make your bet on these turtles", prompt = "Whcih turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow", "cyan", "lightgreen", "turquoise" ]
print(user_bet)

all_turtles = []


y_position = [-140, -100, -60, -20, 20, 60, 100, 140, 180]#y position is set for the turtles to be in different spots
for turtle_index in range (0 , 9): 
    new_turtle  = Turtle()
    new_turtle.speed("fastest")
    new_turtle .shape("turtle")
    new_turtle .color(colors[turtle_index])
    new_turtle .penup()
    new_turtle .goto( x= -330, y = y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
   
    for turtle in all_turtles:
        if turtle.xcor()> 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f"You've Won!! The {winning_color} turtle is the winner!" )
            else:
                print (f"You've Lost! The {winning_color} turtle is the winner!" )


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance) 


screen = Screen()
screen.exitonclick()