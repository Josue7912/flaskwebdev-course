from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp
from wtforms import widgets

class IncidentForm(FlaskForm):
    customer = StringField("Incident Number", validators=[DataRequired(), Regexp('^HP[0-9]{6}$', flags=0, message='Please input valid Incident number')])
    dealer = SelectField("Customer Agent", default="Select your agent", choices=["","Adrian Manolias","Francesc Rebes", "Magdalena Jimenez", "Dalton Molnar"],  validators=[DataRequired()])
    rating = RadioField("Rating", choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')] , widget=widgets.TableWidget(with_table_tag=False), default='5', coerce=int, validators=[DataRequired()])
    comments = TextAreaField("Comments")
    suggestions = TextAreaField("Suggestions")
    submit = SubmitField("Submit")