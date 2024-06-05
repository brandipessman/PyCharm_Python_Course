from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.

PRO of using WTForms over HTML forms is built-in validation. Instead of us 
having to write our own validation code e.g. emails should contain a "@" and a "." 
to be valid or make sure that passwords are minimum of 8 characters, we can use 
all these validation rules straight out of the box from WTForms.
'''

class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators=[DataRequired(), Email(message="Please enter a valid email.")])
    password = PasswordField(label = 'Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters.")])
    submit = SubmitField(label = "Log In")

app = Flask(__name__)
app.secret_key = "secret_string"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
