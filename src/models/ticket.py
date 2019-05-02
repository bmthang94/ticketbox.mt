from src import db

class Ticket(db.Model):

    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(120), nullable=False)
    used = db.Column(db.String())
    order_id= db.Column(db.Integer, db.ForeignKey('orders.id'))
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_type.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))