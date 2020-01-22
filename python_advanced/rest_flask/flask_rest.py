from flask import Flask
from flask_restful import Resource, Api, reqparse

users = [
    {
        'name': 'nick',
        'age': 35,
        'occupation': 'Engineer'
    },
    {
        'name': 'Vera',
        'age': 33,
        'occupation': 'DEV'
    },
    {
        'name': 'Mike',
        'age': 44,
        'occupation': 'SysAdmin'
    },
    {
        'name': 'Sara',
        'age': 27,
        'occupation': 'Nurse'
    },
    {
        'name': 'Otto',
        'age': 66,
        'occupation': 'carpenter'
    },
    {
        'name': 'Jim',
        'age': 44,
        'occupation': 'Teacher'
    }
]

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user['name']:
                return user, 200
        if name == 'all':
            return users, 200
        return 'User not found', 404

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')

        # parse the elements age and occupation to args
        args = parser.parse_args()
        for user in users:
            # if exist, then rewrite
            if name == user['name']:
                user['age'] = int(args['age'])
                user['occupation'] = args['occupation']
                return user, 200
        user = {
            'name': name,
            'age': int(args['age']),
            'occupation': args['occupation']
        }
        users.append(user)

        return user, 201  # created

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')

        args = parser.parse_args()

        for user in users:
            if name == user['name']:
                return f"user {name} already exists", 400  # bad request
        user = {
            'name': name,
            'age': int(args['age']),
            'occupation': args['occupation']
        }
        users.append(user)
        return user, 201 # created

    def delete(self, name):

        for i in range(len(users)):
            if name == users[i]['name']:
                user = users.pop(i)
                return user

        return f'user {name} not found'



api.add_resource(User, '/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
