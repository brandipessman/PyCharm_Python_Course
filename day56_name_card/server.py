from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # Python decorator: go to the home page
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)