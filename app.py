from flask import Flask, render_template, request
from models.score import Score
from models.board import Board

from flask import Flask
app = Flask(__name__)



@app.route("/")
def home():
    board = Board("score.json")
    return render_template("scoreboard.html", board=board),200



if __name__ == "__main__":
    app.run(debug=True)