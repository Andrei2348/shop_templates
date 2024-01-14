from flask import Flask, render_template, flash, request
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
import os
from models import Users, db
from forms import RegistrationForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        try:
            collection = Users(first_name = form.first_name.data,
                                last_name = form.last_name.data,
                                email = form.email.data,
                                password = generate_password_hash(form.password.data))
            db.session.add(collection)
            db.session.commit()
            flash('Пользователь успешно зарегистрирован')
        except:
            flash('Ошибка при регистрации пользователя.')
    return render_template('index.html', my_title = 'Страница регистрации', form=form)


# Ошибка 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', my_title = 'Error')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
