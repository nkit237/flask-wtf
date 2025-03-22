import pytest
import requests
import faker

from data import db_session
from data.users import User

burl = 'http://localhost:8000'

@pytest.fixture
def db_init():
    db_session.global_init("db/mars_explorer.db")


def test_get_one(db_init):
    resp = requests.get(burl + '/api/v1/users/1')
    session = db_session.create_session()
    user = session.query(User).get(1)

    assert resp.json() == {'user': user.to_dict(rules=('-hashed_password', '-jobs'))}


def test_get_one_404():
    resp = requests.get(burl + '/api/v1/users/100')
    assert resp.status_code == 404


def test_get_one_bad_path():
    resp = requests.get(burl + '/api/v1/users/qwerty')
    assert resp.status_code == 404


def test_get_list(db_init):
    resp = requests.get(burl + '/api/v1/users')
    session = db_session.create_session()
    users = session.query(User).all()

    assert resp.json() == {'users': [item.to_dict(only=('id', 'email')) for item in users]}


def test_post_user(db_init):
    fake = faker.Faker()
    user_data = dict(
        name=fake.first_name(),
        surname=fake.last_name(),
        age=fake.random_int(18, 45),
        email=fake.email(),
        position=fake.job(),
        speciality=fake.job(),
        address=fake.address(),
        password='123456'
    )
    resp = requests.post(burl + '/api/v1/users', json=user_data)
    session = db_session.create_session()
    user = session.query(User).get(resp.json()['id'])
    assert user_data['email'] == user.email


def test_post_bad_json_password(db_init):
    fake = faker.Faker()
    user_data = dict(
        name=fake.first_name(),
        surname=fake.last_name(),
        age=fake.random_int(18, 45),
        email=fake.email(),
        position=fake.job(),
        speciality=fake.job(),
        address=fake.address(),
    )
    resp = requests.post(burl + '/api/v1/users', json=user_data)
    assert resp.json() == {"message": {"password": "Missing required parameter in the JSON body or the post body or the query string"}}


def test_post_bad_json(db_init):
    user_data = dict()
    resp = requests.post(burl + '/api/v1/users', json=user_data)
    assert resp.json() == {"message": {"surname": "Missing required parameter in the JSON body or the post body or the query string"}}

def test_delete(db_init):
    session = db_session.create_session()
    users = session.query(User).all()
    resp = requests.delete(burl + f'/api/v1/users/{users[-1].id}')
    assert resp.json() == {'success': 'OK'}

def test_delete_404(db_init):
    resp = requests.delete(burl + f'/api/v1/users/123')
    assert resp.status_code == 404