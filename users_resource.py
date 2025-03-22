from flask import jsonify
from flask_restful import reqparse, abort, Resource

from data import db_session
from data.users import User
from user_parser import parser


def get_or_abort_if_user_not_found(user_id, session=None):
    session = session or db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
        return None
    return user


class UsersResource(Resource):
    def get(self, user_id):
        user = get_or_abort_if_user_not_found(user_id)
        return jsonify({'user': user.to_dict(rules=('-hashed_password', '-jobs'))})

    def delete(self, user_id):
        session = db_session.create_session()
        user = get_or_abort_if_user_not_found(user_id, session)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(only=('id', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            email=args['email'],
            position=args.get('position'),
            speciality=args.get('speciality'),
            address=args.get('address'),
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})