'''Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат'''

from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import os



app = Flask(__name__)

# Страница приветствия
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        field = request.form.get('numb')
        res = make_response(redirect(url_for('result')))
        res.set_cookie('simpleFlask', field)
        return res
    else:
        flash('Введите корректные данные')
    return render_template('index.html', my_title = 'Страница приветствия') 

    
# Страница результатов
@app.route('/result/')
def result():
    value = request.cookies.get('simpleFlask')
    # request.set_cookie('simpleFlask', 'username', max_age = 0)
    print(value)
  
    
    return render_template('result.html', my_title = 'Страница результатов', value = value)




# Ошибка 404
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', my_title = 'Error')


if __name__ == '__main__':
  app.secret_key = os.urandom(24)
  app.run(debug = True)