from flask import Flask, jsonify
import requests
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api_url = 'http://api.openweathermap.org/data/2.5/weather'
q = 'Berlin,deu'
APPID = 'ac5a1ac3f6dda0cfa860b2e6174dd016'

param = {
    'q': q,
    'units':'metric',
    'APPID': APPID
}


class Weather(Resource):
    def get(self):
        r = requests.get(api_url, params=param)
        j = r.json()

        return j, 200


api.add_resource(Weather, '/')

if __name__ == '__main__':
    app.run(debug=True)
