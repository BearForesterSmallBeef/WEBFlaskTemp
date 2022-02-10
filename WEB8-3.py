from flask import Flask, url_for, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "123"


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    param = {'form': form,
             "title": "Авторизация"}
    answer = dict(request.form)
    print(answer)
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("login.html", **param)


@app.route("/success")
def success():
    return render_template("index.html", username="вы успешно авторизованы")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
