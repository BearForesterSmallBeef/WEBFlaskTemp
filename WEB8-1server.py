from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {'username': "Ученик Яндекс.Лицея",
             "title": "Домашняя страница"}
    return render_template('index.html', **param)


@app.route("/old_even")
def old_even():
    param = {"number": 2}
    return render_template("odd_event.html", **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
