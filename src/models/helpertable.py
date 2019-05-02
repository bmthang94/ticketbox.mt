from src import db

event_categories = db.Table('categories',
                      db.Column('event_id', db.Integer, db.ForeignKey(
                          'event.id'), primary_key=True),
                      db.Column('categories_id', db.Integer, db.ForeignKey(
                          'category.id'), primary_key=True)
                      )
event_organizer = db.Table('organizers',
                           db.Column('event_id', db.Integer, db.ForeignKey(
                               'event.id'), primary_key=True),
                           db.Column('organizer_id', db.Integer, db.ForeignKey(
                               'organizer.id'), primary_key=True)
                           )
event_venue = db.Table('venues',
                       db.Column('event_id', db.Integer, db.ForeignKey(
                           'event.id'), primary_key=True),
                       db.Column('venue_id', db.Integer, db.ForeignKey(
                           'venue.id'), primary_key=True)
                       )