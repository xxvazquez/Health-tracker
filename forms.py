from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from models import Food

class IntakeForm(FlaskForm):
    food = SelectField('Food', choices=[], coerce=int, validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add Intake')

    def __init__(self, *args, **kwargs):
        super(IntakeForm, self).__init__(*args, **kwargs)
        self.food.choices = [(food.id, food.name) for food in Food.query.all()]
