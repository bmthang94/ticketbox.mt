from src import db


class Ticket_Types(db.Model):

    __tablename__ = 'ticket_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    open_at = db.Column(db.DateTime, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quota = db.Column(db.Integer)
    ticket = db.relationship('Ticket', backref='type', lazy=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

