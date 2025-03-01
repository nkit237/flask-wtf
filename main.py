from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренажеры', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof = [
        'военные',
        'охрана',
        'производители оружия',
        'испытатели',
        'мясники',
        'телохранители',
        'механики',
        'инженеры',
        'дантисты',
        'повара',
        'хирурги',
        'диктаторы',
    ]
    data = dict(
        title='Список профессий',
        list=list,
        prof_lst=prof,
    )
    return render_template('list_prof.html', **data)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': 'Анкета',
        'surname': 'Сусанин',
        'name': 'Иван',
        'education': '4 класса',
        'profession': 'экскурсовод',
        'sex': 'м',
        'motivation': 'Всегда мечтал застрять на Марсе',
        'ready': 'готов как никогда'
    }
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
