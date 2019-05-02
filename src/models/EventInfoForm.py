from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
import phonenumbers
from wtforms_components import DateTimeField


def validate_organizer_phone(FlaskForm, field):
    print( field.data.isdigit())
    if len(field.data) > 11 or not field.data.isdigit():
        raise ValidationError('Invalid phone number.')
    try:
        input_number = phonenumbers.parse(field.data)
        if not (phonenumbers.is_valid_number(input_number)):
            raise ValidationError('Invalid phone number.')
    except:
        input_number = phonenumbers.parse("+84"+field.data)
        if not (phonenumbers.is_valid_number(input_number)):
            raise ValidationError('Invalid phone number.')
            
class EventInfo(FlaskForm):
    
    event_name = StringField('Event name', validators=[DataRequired()])
    event_start_time = StringField('Start',validators=[DataRequired()])
    event_end_time = StringField('End', validators=[DataRequired()])
    event_description = StringField(
        'Event informaiton', validators=[DataRequired()])
    venue_name = StringField('Venue name ', validators=[DataRequired()])
    venue_address = StringField('Address', validators=[DataRequired()])
    organizer_name = StringField('Organizer name', validators=[DataRequired()])
    organizer_description = StringField(
        'Organizer Description', validators=[DataRequired()])
    organizer_phone = StringField(
        'Phone', validators=[DataRequired(), validate_organizer_phone])
    organizer_email = StringField(
        'Email', validators=[DataRequired(), Email()])
    # categories = StringField('Categories', validators=[DataRequired()])
    categories = SelectField('Category: ',  coerce=int)
    submit = SubmitField('Create')