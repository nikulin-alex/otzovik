from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'SECRET_KEY'

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)
    image = db.Column(db.String(255),nullable=False)
    reviews = db.relationship('Review',back_populates='movie')
class Review(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    text = db.Column(db.Text,nullable=False)
    created_date = db.Column(db.DateTime,default=datetime.utcnow)
    score = db.Column(db.Integer,nullable=False)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id',ondelete='CASCADE'))
    movie = db.relationship('Movie',back_populates='reviews')
with app.app_context():
    db.create_all()