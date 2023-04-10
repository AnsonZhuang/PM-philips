# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from apps.user import blueprint
from flask import render_template, request, g
from flask_login import login_required, current_user
from apps.database.query import query_projects_by_user, query_created_projects_by_user, query_resource_by_user_project, \
    prepare_resource_table_data_user
from apps.authentication.models import User, Project
from jinja2 import TemplateNotFound


@blueprint.route('/personal-info')
@login_required
def personal_info():
    return render_template('user/personal_info.html')


@blueprint.route('/involved-projects')
@login_required
def involved_projects():
    project_list = prepare_resource_table_data_user(current_user.id)
    return render_template('user/involved_projects.html', resource=project_list)


@blueprint.route('/created-projects')
@login_required
def created_projects():
    projects = query_created_projects_by_user(current_user.id)
    print(projects)
    return render_template('user/created_projects.html')


@blueprint.route('/my-team')
@login_required
def my_team():
    return render_template('user/my_team.html')


@blueprint.route('/add-example-project')
@login_required
def add_example_project():
    return render_template('user/involved_projects.html')
