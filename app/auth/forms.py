from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Användarnamn'), validators=[DataRequired()])
    password = PasswordField(_l('Lösenord'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Kom ihåg mig'))
    submit = SubmitField(_l('Logga in'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Använarnamn'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Lösenord'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Upprepa lösenord'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Registrera'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Använd ett annat användarnamn.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Använd en annan mailadress.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Återställ lösenord'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Lösenord'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Upprepa Lösenord'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
