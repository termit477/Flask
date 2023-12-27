from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


db = SQLAlchemy()


class ContactForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100)])
    password_validate = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])


class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
