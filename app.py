from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}"
    
with app.app_context():
    db.create_all() 

@app.route('/',methods=['GET', 'POST'])
def index():
    # Add a new task
    if(request.method == 'POST'):
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred while adding a new task: {e}")
            return f"An error occurred while adding a new task: {e}"

    # Get all tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"An error occurred while deleting a task: {e}")
        return f"An error occurred while deleting a task: {e}"

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"An error occurred while updating a task: {e}")
            return f"An error occurred while updating a task: {e}"
    else:
        return render_template('update.html', task=task)




if __name__ == '__main__':
     # create database tables if not exist
    app.run(debug=True)


