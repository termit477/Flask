# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_6.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    if age > 17:
        return render_template('welcome.html', name=name)
    else:
        return render_template('error.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)