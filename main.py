"""
name the States game from day 25 of 100 days of Code
using pandas and turtle to create a game where you
have to name all 50 states to win, correct names are
written on a map using turtle, pandas is used to check the
coordinates to determine where the name should be written
based on the data in the 50 states csv
"""
import turtle as t
import pandas as pd

data = pd.read_csv('50_states.csv')
game_on = True
right_guess = 0
wrong_guess = 0
correct_answers = []

image = 'blank_states_img.gif'
screen = t.Screen()
screen.title('USA states name game')

screen.addshape(image)
t.shape(image)

state_writer = t.Turtle()
state_writer.hideturtle()

score = t.Turtle()
score.penup()
score.hideturtle()

while game_on:
    answer_state = screen.textinput(title=f'{right_guess} out of 50 State Names!', prompt='Enter a state name:').title()

    if answer_state == 'Exit':
        game_on = False
        break

    check = data[data.state == answer_state]

    state_writer.penup()
    if answer_state not in correct_answers:
        try:
            state_writer.goto(int(check.x), int(check.y))
            state_writer.pendown()
            state_writer.write(answer_state)

            right_guess += 1
            correct_answers.append(answer_state)
            if right_guess == 50:
                print('YOU WIN!')
                game_on = False

        except TypeError:
            # handle the empty data set that is returned
            wrong_guess += 1
            if wrong_guess == 2:
                print('TOO MANY WRONG!')
                game_on = False
            continue


missed_states = [s for s in data.state if s not in correct_answers]

tracking_dict = {'states forgotten': missed_states}
# can't track both remembered and forgotten because the len must be the same here :(

saved_data = pd.DataFrame.from_dict(tracking_dict)
saved_data.to_csv('last_game.csv')
