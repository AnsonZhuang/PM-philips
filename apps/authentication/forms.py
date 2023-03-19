# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, IntegerField
from wtforms.validators import Email, DataRequired, length, NumberRange, EqualTo
from .models import User


# Login

class LoginForm(FlaskForm):
    email = StringField('Email', id='email_login', validators=[DataRequired(message="Please input your email"), Email(message="Invalid email format")])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired(message="Please input your password")])

    def validate_email(self, field):
        email = field.data
        user_model = User.query.filter_by(email=email).first()
        if not user_model and "email" not in self.errors:
            print("The Email has not been used for registration.")
            raise ValidationError("The Email has not been used for registration.")


# Register

class CreateAccountForm(FlaskForm):
    id = StringField('id', id='id_create', validators=[DataRequired(message="Please input your id")])
    username = StringField('Username', id='username_create',
                           validators=[DataRequired(message="Please input your username"), length(min=2, max=36)])
    email = StringField('Email', id='email_create',
                        validators=[DataRequired(message="Please input your email"), Email(message="Invalid email format"), length(max=64)])
    password = PasswordField('Password', id='pwd_create',
                             validators=[DataRequired(message="Please input your password"), length(min=6, max=24)])
    password_confirm = PasswordField('Password Confirm', id='pwd_cfm_create',
                                     validators=[DataRequired(message="Please confirm your password"),
                                                 EqualTo("password", message="Two passwords are inconsistent")])

    def validate_id(self, field):
        id = int(field.data)
        if id < 0 or id > 999999999:
            print("Your id must be 0-999999999")
            raise ValidationError("Your id must be 0-999999999")
