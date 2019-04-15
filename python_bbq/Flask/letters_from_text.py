from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)


@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title="Entry")

@app.route('/')
def printHello():
    return "Hello"


@app.route('/search4', methods=['POST'])
def search4() -> 'str':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results: '
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results
                           )


app.run()
