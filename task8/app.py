'''Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".'''

from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import os


app = Flask(__name__)

# Страница приветствия
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('welcome', username = username))
    return render_template('index.html', my_title = 'Главная страница') 

    
# Страница результатов
@app.route('/welcome/')
def welcome():
    username = request.args.get('username', None)
    flash(f'Добро пожаловать {username}!')
    return render_template('result.html', my_title = 'Страница приветствия')


# Ошибка 404
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', my_title = 'Error')


if __name__ == '__main__':
  app.secret_key = os.urandom(24)
  app.run(debug = True)