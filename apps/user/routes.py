# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from apps.user import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/personal-info')
@login_required
def personal_info():
    return render_template('user/personal_info.html')


@blueprint.route('/my-projects')
@login_required
def my_projects():
    return render_template('user/my_projects.html')


@blueprint.route('/my-team')
@login_required
def my_team():
    return render_template('user/my_team.html')


@blueprint.route('/create-example-project')
@login_required
def create_example_project():
    project_id = 15
    project_name = 'example_project'
    create_resource_table(project_id, project_name)
    return render_template('user/my_projects.html')


def create_resource_table(project_id, project_name):
    table_name = "project_resource_" + project_id
    columns = {
        "__tablename__": table_name,
        "id": db.Column(db.Integer, primary_key=True, autoincrement=False),
        "Year": db.Column(db.Integer),
        "Jan": db.Column(db.Integer),
        "Feb": db.Column(db.Integer),
        "Mar": db.Column(db.Integer),
        "Apr": db.Column(db.Integer),
        "May": db.Column(db.Integer),
        "Jun": db.Column(db.Integer),
        "Jul": db.Column(db.Integer),
        "Aug": db.Column(db.Integer),
        "Sep": db.Column(db.Integer),
        "Oct": db.Column(db.Integer),
        "Nov": db.Column(db.Integer),
        "Dec": db.Column(db.Integer),
    }
    # 由于使用flask migrate 必须创建对应模型来创建表
    new_model = type(project_name, (db.Model,), columns)
    db.create_all()
    return table_name
