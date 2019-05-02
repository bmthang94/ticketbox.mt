from src import db
from src.models.helpertable import event_categories, event_organizer, event_venue


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    venue = db.relationship(
        'Venue',
        secondary=event_venue,
        lazy='subquery',
        backref=db.backref('events', lazy=True)
    )
    organizers = db.relationship(
        'Organizer',
        secondary=event_organizer,
        lazy='subquery',
        backref=db.backref('events', lazy=True)
    )
    ticket_types = db.relationship(
        'Ticket_Types',
        backref='ticket_types',
        lazy=True) 
    categories = db.relationship(
        'Category',
        secondary=event_categories,
        lazy='subquery',
        backref=db.backref('events', lazy=True)
    )
