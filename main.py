from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return """Человечество вырастает из детства.</br>
        Человечеству мала одна планета.</br>
        Мы сделаем обитаемыми безжизненные пока планеты.</br>
        И начнем с Марса!</br>
        Присоединяйся!"""


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, марс!</h1>
                    <img src="/static/img/mars.jpg" alt="Морс">
                    <br>это не марс
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
