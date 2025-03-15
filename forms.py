from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    address = StringField("Адрес")
    submit = SubmitField('Зарегистрироваться')

class AddJob(FlaskForm):
    job = StringField('Что делать?')
    # team_leader = SelectField('Ответственный')
    team_leader = IntegerField('Ответственный')
    work_size = IntegerField('Объём работы, ч')
    collaborators = StringField('Сообщники')
    start_date = DateField('Дата начала')
    end_date = DateField('Дата окончания')
    is_finished = BooleanField('Завершено')
    submit = SubmitField('Добавить')