from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/') # Python decorator: go to the home page
def home():
    year = datetime.date.today().year
    my_name = "Brandi Pessman"
    random_number = random.randint(1, 10)
    return render_template("index.html", num = random_number, current_year = year, name = my_name)

@app.route('/guess/<name>') # Python decorator: go to the home page
def guess(name):
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data['age']
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data['gender']
    return render_template("guess.html", age=age, name=name, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug = True)