from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wil you bet on?:")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):      
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.goto(-25,0)
                turtle.write("YOU WIN", align="right", font=("Cooper Black", 25, "italic"))

            else:
                turtle.goto(25,0)
                turtle.write("YOU LOSE", align="left", font=("Cooper Black", 25, "italic"))
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()