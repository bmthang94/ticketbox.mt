from src import db


class Organizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    # event = db.relationship('Event', backref='image', lazy=True)