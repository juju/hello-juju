from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE

db = SQLAlchemy(app)

class Greeting(db):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"<Greeting {self.id} ({self.created_at})>"

def init():
    db.create_all()

def increment_greetings():
    db.session.add(Greeting())
    db.session.commit()

@app.route('/greetings')
def count_greetings():
    global db

    return {"greetings": db.session.query(func.count(Greeting.id)).scalar() }

@app.route('/')
def hello_world():
    increment_greetings()
    return 'Hello Juju!\r\n'


if __name__ == '__main__':
    app.run()
