from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return {'Whale,' : 'Hello there!'}


@app.route('/hello2/')
def hello2():
    return jsonify(hello2 = "Hello World 2", Null = None)


if __name__ == '__main__':
    app.run(debug=True)
