from flask import Flask, render_template, flash, session, request, redirect, url_for, jsonify

app = Flask(__name__)

catalog = {"Обувь": ["Кроссовки", "Туфли", "Сандалии", "Сапоги"],
           "Одежда":["Рубашка","майка", "Свитер","Брюки"],
           "Куртки": ["Зимняя куртка","Пальто", "Шуба", "Ветровка"]
          }

title = tuple(catalog.keys())



# Главная страница проекта
@app.route('/index/')
@app.route('/')
def index():
  return render_template('index.html', my_title = 'Магазин одежды', catalog = catalog)


@app.route('/shoes/')
def shoes():
  
  return render_template('pattern.html', my_title = 'Обувь на сайте', title = title[0], catalog = catalog["Обувь"])


@app.route('/clothes/')
def clothes():
  return render_template('pattern.html', my_title = 'Одежда на сайте', title = title[1], catalog = catalog["Одежда"])


@app.route('/jackets/')
def jackets():
  return render_template('pattern.html', my_title = 'Куртки на сайте', title = title[2], catalog = catalog["Куртки"])


# Ошибка 404
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', my_title = 'Error')


if __name__ == '__main__':
  app.run(debug = True)