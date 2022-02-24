from flask import Flask, url_for

app = Flask(__name__)
image_link = "http://astrobel.ru/images/stories/foto/2018/ClipBoard-2.jpg"


@app.route("/")
def main_menu():
    return \
        f'''
        <h1>Миссия Колонизация Марса</h1>
        <ol>
        <li><a href="http:\\promotion">Promotion</a>
        <li><a href="http:\\index">Index</a>
        <li><a href="http:\\image_mars">Image of mars</a> 
        </ol>
        '''


@app.route("/index")
def index():
    return f"""<h1>И на Марсе будут яблони цвести!</h1>"""


@app.route("/promotion")
def promotion():
    return \
        f"""
        <div>Человечество вырастает из детства.<br>
        Человечеству мала одна планета.<br>
        Мы сделаем обитаемыми безжизненные пока планеты.<br>
        И начнем с Марса!<br>
        Присоединяйся!</div>"""


@app.route("/image_mars")
def image_mars():
    return \
        f'''
        <title>Привет, Марс!</title>
        <h1>Жди нас, Марс!</h1>
        <img src={image_link} alt="Марс сломался :(" align="middle" height=350 width=500>
        <div>Вот она какая, красная планета</div>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')