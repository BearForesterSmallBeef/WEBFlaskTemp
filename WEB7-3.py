from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def main_menu():
    return f"""<h1>Миссия Колонизация Марса</h1>"""


@app.route("/index")
def index():
    return f"""<h1>И на Марсе будут яблони цвести!</h1>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')