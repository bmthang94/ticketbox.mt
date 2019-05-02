from flask import Blueprint, render_template, request
from src.models.EventInfoForm import EventInfo
from src.models.EventInfoForm import TicketType
from src.models.event import Event
from src.models.venue import Venue
from src.models.organizer import Organizer
from src.models.categories import Category
from src import db
from datetime import datetime

events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='../../templates/events')


@events_blueprint.route('/add/info', methods=['GET', 'POST'])
def addInfo():
    form = EventInfo()
    categories = Category.query.all()
    form.categories.choices = [(cat.id, cat.name) for cat in categories]
    if form.validate_on_submit():
        organizer = Organizer(
            name=form.organizer_name.data,
            description=form.organizer_description.data,
            phone=form.organizer_phone.data,
            email=form.organizer_email.data,
        )
        venue = Venue(
            name=form.venue_name.data,
            address=form.venue_address.data
        )
        categories = Category(
            name=form.categories.data,
        )
        multiRow = [
            organizer,
            venue,
            categories
        ]
        db.session.bulk_save_objects(multiRow)
        db.session.commit()
        event = Event(
            name=form.event_name.data,
            # # start_time=datetime.strptime(
            # #     "2019-02-02 10:00", '%Y-%m-%d %H:%M'),
            # # end_time=datetime.strptime(
            # #     "2019-02-02 10:00", '%Y-%m-%d %H:%M'),
            # start_time=datetime.strptime(
            #     form.event_start_time.data, '%Y-%m-%d %H:%M'),
            # end_time=datetime.strptime(
            #     form.event_end_time.data, '%Y-%m-%d %H:%M'),
            description=form.event_description.data
        )
        event.organizer.append(organizer)
        event.ticket_types.append()
        event.categories.append(categories)

        db.session.add(event)
        db.session.commit()
    
    return render_template('createEvent.html', 
    vars={
        "form": form,
        "customField": 4,
        }
    )


@events_blueprint.route('/add/ticket', methods=['GET', 'POST'])
def addTicket():
    
    return render_template('createEvent.html', 
    vars={
        "form": form,
        "customField": 4,
        }
    )

@events_blueprint.route('/list')
def list():
    return "All Event"
