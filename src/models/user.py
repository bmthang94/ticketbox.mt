from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    ticket = db.relationship('Ticket', backref='ticket', lazy=True)
    order = db.relationship('Orders', backref='order', lazy=True)
