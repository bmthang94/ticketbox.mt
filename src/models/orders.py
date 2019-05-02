from src import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    status = db.Column(db.String(120), unique=True, nullable=False)
    ticket = db.relationship('Ticket', backref='orders', lazy=True)
