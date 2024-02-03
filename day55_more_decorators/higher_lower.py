from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def pick():
    return ("<h1>Guess a number between 0 and 9<h1/>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

number = random.randint(0,9)
print(number)

@app.route('/<int:guess>')
def check(guess):
    if guess < number:
        return ('<h1>Too Low!<h1/>'
                '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif guess > number:
        return ('<h1>Too High!<h1/>'
                '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1>Youu found me!<h1/>'
                '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

if __name__ == "__main__":
    app.run(debug = True) # same as saying flask run in terminal