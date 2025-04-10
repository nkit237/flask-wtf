from flask import Flask, render_template, redirect, request, make_response, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_restful import Api
from data import db_session
from data.jobs import Jobs
from data.users import User
from data import jobs_api
from forms import RegisterForm, LoginForm, AddJob
from flask import make_response
from users_resource import UsersResource, UsersListResource

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.register_blueprint(jobs_api.blueprint)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        job = Jobs(
            job = form.job.data,
            team_leader = form.team_leader.data,
            work_size=form.work_size.data,
            collaborators = form.collaborators.data,
            start_date = form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data
        )
        db_sess = db_session.create_session()
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    # db_sess = db_session.create_session()
    # users = db_sess.query(User).all()
    # form.team_leader.choices = [(user.id, user.name) for user in users]
    return render_template('add_job.html', title='Доб раб', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
