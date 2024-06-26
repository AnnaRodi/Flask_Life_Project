# This is a sample Python script.https://stepik.org/lesson/534531/step/2?unit=527649

from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(20, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    life = GameOfLife()
    life.form_new_generation()
    return render_template('live.html', life = life)

if __name__=='__main__':
    app.run(debug=True)