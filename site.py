import flask
import game

app = flask.Flask(__name__)

@app.route('/')

def index():
    return "haha, You can't use tkinter in web browser. YIKES"

if __name__ == '__main__':
    app.run(debug=True)

