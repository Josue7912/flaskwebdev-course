from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, SubmitField
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired, Regexp


class IncidentForm(FlaskForm):
    customer = StringField("Customer", validators=[DataRequired(), Regexp('^[A-Za-z0-9]*$', 0, 'Incident number must have only letters and numbers')])
    dealer = StringField("Customer", validators=[DataRequired()])
    rating = RadioField("Rating", choices=['0','1','2','3','4','5','6','7','8','9','10'] , coerce=int, validators=[DataRequired()])
    comments = TextAreaField("Customer")
    suggestions = TextAreaField("Customer")
    submit = SubmitField("Submit")