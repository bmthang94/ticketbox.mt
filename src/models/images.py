from src import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(), nullable=False)
    event = db.relationship('Event', backref='event', lazy=True)
