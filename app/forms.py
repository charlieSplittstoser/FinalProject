from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms import StringField, SubmitField, SelectField, validators
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address is already in use.')

class LibraryForm(FlaskForm):
    def validate_library(form, field):
        if (len(field.data) == 0):
            raise ValidationError(message)

    id_type = SelectField('ID', choices=[("Default", "Select"), ("isbn","isbn"), ("lccn", "lccn"), ("oclc", "oclc"), ('olid', "olid")], render_kw={'class': 'form-control'})
    id_value = StringField('Value', [validators.Required(message="Please enter value.")],render_kw={'class': 'form-control'})
    submit = SubmitField("Submit")