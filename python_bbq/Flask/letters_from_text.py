from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title="Entry")


@app.route('/')
def print_hello():
    return "Hello"

# '''old function'''
# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         print(req, res, file=log)

def log_request(req: 'flask_request', res: str) -> None:
    '''Log details of the web request and the results'''
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': '',
                'database': 'vsearchlogdb',
                }
    import mysql.connector

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, )
                   )
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def search4() -> 'str':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    title = 'Here are your results: '
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


app.run()
