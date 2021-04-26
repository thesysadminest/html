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


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, марс!</h1>
                    <img src="/static/img/mars.jpg" alt="Морс">
                    <div class="alert alert-info" role="alert">
                      Сейчас я прыгну
                    </div>
                    <div class="alert alert-success" role="alert">
                      На гараж
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Скоро космос
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Будет наш!
                    </div>
                    <br>конец стиха
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
