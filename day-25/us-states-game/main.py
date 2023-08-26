import pandas
import turtle

states_df = pandas.read_csv("50_states.csv")
states = states_df.state.tolist()

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

score = 0
correct_guesses = []
while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 States", prompt="What's another state's name? ").title()
    # if answer_state == "Exit":
    #     not_guessed = []
    #     for state in states:
    #         if state not in correct_guesses:
    #             not_guessed.append(state)
    #     new_data = pandas.DataFrame(not_guessed)
    #     new_data.to_csv("states_to_learn.csv")
    #     break

    if answer_state == "Exit":
        not_guessed = [state for state in states if state not in correct_guesses]
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in correct_guesses:
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        state_row = states_df[states_df.state == answer_state]
        label.goto(int(state_row.x), int(state_row.y))
        label.write(answer_state)
        correct_guesses.append(answer_state)
        score += 1

# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
