from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def show_entry():
    return render_template('entry.html', the_title='welcome to bmi-online' )


def log_request(req: 'flask_request', res: str) -> None:
    '''Log details of the web request and the results'''
    dbconfig = {'host': '127.0.0.1',
                'user': 'user1',
                'password': 'pass1',
                'database': 'bmiwebdb',
                }
    import mysql.connector

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
              (WEIGHT, HEIGHT, IP, BROWSER_STRING, BMI)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['weight'],
                          req.form['height'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, )
                   )
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def bmi_cal():
    weight = request.form['weight']
    height = request.form['height']
    bmi = round(float(weight) / ((float(height) / 100) ** 2), 2)
    bmi = str(bmi)
    log_request(request, bmi)
    return render_template('results.html', the_title='Here your results: ', the_weight=weight,
                           the_height=height, the_results=bmi)


app.run(debug=True)
