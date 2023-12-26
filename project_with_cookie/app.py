from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import os



app = Flask(__name__)


# Главная страница
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == 'POST':
    username = request.form.get('username')
    email = request.form.get('email')
    if username and email:
      res = make_response(redirect(url_for('welcome')))
      res.set_cookie('simpleFlask', username)
      return res
    else:
      flash('Введите корректные данные')
  return render_template('index.html', my_title = 'Страница данных пользователя')



# Страница приветствия
@app.route('/welcome/', methods = ['GET', 'POST'])
def welcome():
  if request.cookies.get('simpleFlask'):
    if request.method == 'POST':
      res = make_response(redirect(url_for('index')))
      res.set_cookie('simpleFlask', 'username', max_age = 0)
      return res
  else:
    return redirect(url_for('index'))
  
  value = request.cookies.get('simpleFlask')
  return render_template('welcome.html', my_title = 'Страница приветствия', username = value) 


# Ошибка 404
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', my_title = 'Error')


if __name__ == '__main__':
  app.secret_key = os.urandom(24)
  app.run(debug = True)