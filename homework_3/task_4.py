# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from models import ContactForm, db, Authentication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'secretkey'
db.init_app(app)
csrf = CSRFProtect(app)


def add_user(name, mail, password):
    user = Authentication(name=name, mail=mail, password=password)
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    db.create_all()
    print('База успешно создана.')
    form = ContactForm()
    form_errors = []
    if request.method == 'POST' and form.validate():
        name = form.name.data
        mail = form.email.data
        if Authentication.query.filter(Authentication.name == name).count() > 0:
            form_errors.append(f'Имя {name} уже занят.')
        if Authentication.query.filter(Authentication.mail == mail).count() > 0:
            form_errors.append(f'Такой email {mail} уже зарегистрирован.')
        else:
            print(f'Пользователь {name} добавлен.')
            add_user(name, form.email.data, form.password.data)
            form_notifications = [f'Пользователь {name} зарегистрирован.']
            return render_template('login_form.html', form=form, form_notifications=form_notifications)
    return render_template('login_form.html', form=form, form_errors=form_errors)
