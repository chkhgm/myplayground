import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_answers = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

text = turtle.Turtle()
text.penup()
text.hideturtle()

def make_title():
    count = len(correct_answers)
    if count > 0:
        return f"{count}/50 States Correct"
    else:
        return  "Guess the state"


while len(correct_answers) < 50:
    answer_state = screen.textinput(title=make_title(), prompt="what's another state name?").title()
    if answer_state in all_states:
        correct_answers.append(answer_state.title())
        new_state = data[data["state"] == answer_state.title()]
        text.goto(int(new_state.x), int(new_state.y))
        text.write(new_state.state.item())



screen.exitonclick()
