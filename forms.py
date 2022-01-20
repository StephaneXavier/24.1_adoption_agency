from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,IntegerField,BooleanField, SelectField, DecimalRangeField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

age_list = [n for n in range(31)]
age_list.insert(0,'-') 

class AddPet(FlaskForm):
    """Form to add new pet"""
    pet_name = StringField('Pet name', validators =[InputRequired(message='Name is required')] )
    species = SelectField ('Species', choices=['-','cat','dog','porcupine'], validators = [InputRequired(message='Species is required')])
    photo_url = StringField('Photo url', validators = [Optional(),URL(message = 'Invalid URL')])
    age = SelectField('Age', choices = age_list ,validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField(default = True)
