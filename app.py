from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#set up application
app = Flask(__name__)
#initializing a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #column to hold each task
    content = db.Column(db.String(200), nullable=False)
    # any time a new to do is entered, the dstetime will automatically be set to the current datetime.
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        #create a todo object
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'FUCK'
    else:
        #returns all the to dos sorted based on date created
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        #redirect to the homepage
        return redirect('/')
    except:
        return 'Fuck it lads'


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    


if __name__ == "__main__":
    app.run(debug=True)