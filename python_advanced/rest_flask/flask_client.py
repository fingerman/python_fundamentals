from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        my_json = request.get_json()
        return jsonify(you_sent = my_json)
    else:
        return jsonify(about = 'Hello World holala !')



@app.route('/mult10/<int:num>', methods=['GET'])
def mult10(num):
    return jsonify(result=num*10)




if __name__ == '__main__':
    app.run(debug=True)
