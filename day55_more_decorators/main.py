from flask import Flask
app = Flask(__name__)

@app.route('/') # Python decorator: go to the home page
def hello_world():
    return 'Hello, World!'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    print(f"Hello there {name}, you are {number} years old!")

inputs = eval(input())
def logging_decorator(fn):
  def wrapper(*args):
    print(f"You called: {fn.__name__}{args}")
    results = fn(args[0], args[1], args[2])
    print(f"It returned: {results}")
  return wrapper

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])

if __name__ == "__main__":
    app.run(debug = True) # same as saying flask run in terminal