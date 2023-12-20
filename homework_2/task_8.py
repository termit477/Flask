# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


from flask import Flask, redirect, render_template, request, flash, url_for
import secrets


app = Flask(__name__)


secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')

        return redirect(url_for('form'))

    return render_template('form_8.html')


if __name__ == '__main__':
    app.run(debug=True)