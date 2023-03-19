# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import User, UserPermission

from apps.authentication.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and 'login' in request.form:
        if login_form.validate():
            # read form data
            email = request.form['email']
            password = request.form['password']

            # Locate user
            user = User.query.filter_by(email=email).first()

            # Check the password
            if user and verify_pass(password, user.password):

                login_user(user)
                return redirect(url_for('authentication_blueprint.route_default'))

            # Something (user or pass) is not ok
            return render_template('accounts/login.html',
                                   msg='Wrong user or password',
                                   form=login_form)
        else:
            error_message = next(iter(login_form.errors.values()))[0]
            return render_template('accounts/login.html',
                                   form=login_form,
                                   msg=error_message)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html', form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if request.method == 'POST' and 'register' in request.form:
        if create_account_form.validate():
            id = request.form['id']
            username = request.form['username']
            email = request.form['email']

            # Check id exists
            user = User.query.filter_by(id=id).first()
            if user:
                return render_template('accounts/register.html',
                                       msg='ID already registered',
                                       success=False,
                                       form=create_account_form)

            # Check username exists
            user = User.query.filter_by(username=username).first()
            if user:
                return render_template('accounts/register.html',
                                       msg='Username already registered',
                                       success=False,
                                       form=create_account_form)

            # Check email exists
            user = User.query.filter_by(email=email).first()
            if user:
                return render_template('accounts/register.html',
                                       msg='Email already registered',
                                       success=False,
                                       form=create_account_form)

            # else we can create the user
            user = User(**request.form)
            user_permission = UserPermission(id=id, access_ALL=False, access_RD=False, access_PMO=False,
                                             access_SW=False, access_VV=False, access_SYS=False, access_HW=False,
                                             manage_ALL=False, manage_RD=False, manage_PMO=False, manage_SW=False,
                                             manage_VV=False, manage_SYS=False, manage_HW=False, config_ALL=False,
                                             config_RD=False, config_PMO=False, config_SW=False, config_VV=False,
                                             config_SYS=False, config_HW=False)
            db.session.add(user)
            db.session.commit()

            # Delete user from session
            logout_user()

            return render_template('accounts/register.html',
                                   msg='User created successfully.',
                                   success=True,
                                   form=create_account_form)

        else:
            error_message = next(iter(create_account_form.errors.values()))[0]
            return render_template('accounts/register.html', form=create_account_form, msg=error_message)
    else:
        return render_template('accounts/register.html', form=create_account_form)



@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('pages/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('pages/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('pages/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('pages/page-500.html'), 500
