from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
