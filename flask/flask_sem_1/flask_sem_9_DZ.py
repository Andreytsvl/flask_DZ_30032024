# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('velo.html')


@app.route('/velo_zip/')
def velo_zip():
    return render_template('velo_zip.html')


@app.route('/velo_merch/')
def velo_merch():
    return render_template('velo_merch.html')


if __name__ == '__main__':
    app.run()
