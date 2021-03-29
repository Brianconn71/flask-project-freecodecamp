from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#set up application
app = Flask(__name__)
#initializing a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.model):
    id = db.Column(db.Integer, primary_key)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)