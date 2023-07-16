from flask import Flask,render_template
from classes import Jogo


app = Flask(__name__)
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Skyrim', 'A', 'C')
jogo3 = Jogo('D', 'BN', '@')
jogo4 = Jogo('A','D',"2323141")
listadejogos = [jogo1, jogo2, jogo3,jogo4]

@app.route('/')
def hello():
    return render_template('index.html',jogosdentrodalista=listadejogos)

if __name__ == '__main__':
    app.run(debug=True)
