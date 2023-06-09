# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from apps.user import blueprint
from flask import render_template, request, g
from flask_login import login_required, current_user
from apps.authentication.models import User, Project
from jinja2 import TemplateNotFound


@blueprint.route('/personal-info')
@login_required
def personal_info():
    return render_template('user/personal_info.html')