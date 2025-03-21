from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=False)
parser.add_argument('speciality', required=False)
parser.add_argument('address', required=False)
parser.add_argument('email', required=True)
parser.add_argument('password', required=True)