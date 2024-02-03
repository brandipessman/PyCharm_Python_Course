from flask import Flask
app = Flask(__name__)

@app.route('/') # Python decorator: go to the home page
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug = True) # same as saying flask run in terminal