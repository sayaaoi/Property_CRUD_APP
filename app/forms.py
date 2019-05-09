from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, FloatField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError
from app.models import Property, PropertySchema

class PropertyFrom(FlaskForm):
    PropertyID = IntegerField('Property ID:')
    PropertyName = StringField('Property Name:', validators=[DataRequired(), validators.Length(max=20)])
    City = StringField('City:', validators=[DataRequired(),validators.Length(max=30)])
    MarketValue = FloatField('Market Value:', validators=[DataRequired()])
    Cost = FloatField('Cost:', validators=[DataRequired()])
    Submit = SubmitField('Insert Data')

