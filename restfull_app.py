# from flask import Flask
from flask_restful import Api

from app import app
from data import db_session
from users_resource import UsersResource, UsersListResource


def main():
    db_session.global_init('db/mars_explorer.db')
    # app = Flask(__name__)
    api = Api(app)
    api.add_resource(UsersResource, '/api/v1/users/<int:user_id>')
    api.add_resource(UsersListResource, '/api/v1/users')

    app.run('localhost', 8000)


if __name__ == '__main__':
    main()