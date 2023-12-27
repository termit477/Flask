# Создайте форму для регистрации пользователей в вашем веб-приложении.
# Форма должна содержать следующие поля: имя пользователя, электронная почта, 
# пароль и подтверждение пароля.
# Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об успешной регистрации.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from models import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    form_notifications = []
    if request.method == 'POST' and form.validate():
        name = form.name.data
        mail = form.email.data
        form_notifications.append(f'Пользователь {name} {mail} зарегистрирован')
        return render_template('login_form.html', form=form, form_notifications=form_notifications)
    return render_template('login_form.html', form=form)
