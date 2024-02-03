# Python Decorator
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()
        function()
        # do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

# say_hello()
# say_bye()
# say_greeting()

decorated_function = delay_decorator(say_greeting)
decorated_function()

