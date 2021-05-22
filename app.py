from boggle import Boggle
from flask import Flask, session, request, render_template, jsonify
from english_words import english_words_set

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "v3rysecret"

game = Boggle()
starting_message = "Start Guessing!"

@app.route('/')
def home():
    session['board'] = game.make_board()
    # print(session.get('board', 'not set'))
    high_score = session.get('highscore', 0)
    attempts = session.get('attempt', 0)

    return render_template('index.html', board =session.get('board', 'not set'), highscore = high_score, attempt=attempts)

@app.route('/submit/<guess>', methods = ["POST"])
def handle_submit(guess):
    if guess in english_words_set:
        response = jsonify(result = boggle_game.check_valid_word(session.get('board'), guess), word = guess)
        return response
    else:
        return
   
@app.route('/score', methods = ["POST"])
def score():
    try:
        request.json['score']
        score = request.json['score']
    except: 
        score = 0

    high_score = session.get('highscore', 0)
    attempts = session.get('attempt', 0)

    session['attempt'] = attempts + 1
    session['highscore'] = max(score, high_score)
    
    return jsonify(record=score)




