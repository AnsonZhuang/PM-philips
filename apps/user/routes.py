# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from apps.user import blueprint
from flask import render_template, request, g
from flask_login import login_required, current_user
from apps.authentication.models import Project, UserToProject
from jinja2 import TemplateNotFound

dict={}

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


@blueprint.route('/add-example-project')
@login_required
def add_example_project():
    project_id = 15
    project_name = 'example_project'
    # 1 Create entry in Project table for the example project
    new_project = Project(id=project_id, name="project_"+str(project_id), priority_id=1, product_id=1, creator_id=current_user.id,
                          manager_id=current_user.id, create_date="2023-03-20", status_update_date="2023-03-22", launch_date="2023-03-26",
                          end_date="2023-08-15", visible=True, status_id=1, description="No description", plan="",
                          resource_table_name="project_resource_" + str(project_id))
    db.session.add(new_project)
    db.session.commit()
    # 2 Create new Project resource table for the example project(if not exists)
    # sql = "CREATE TABLE IF NOT EXISTS '" + get_resource_table_name(project_id) + "'('"+


    # create_resource_table(project_id, project_name)
    return render_template('user/my_projects.html')
#
#
# @blueprint.route('/join-example-project')
# @login_required
# def join_example_project():
#     project_id = 15
#     project_name = 'example_project'
#     table_name = get_resource_table_name(project_id)
#     current_project=Project.query.filter_by(id=project_id).first()
#     # 1 Add user-project to UserToProject
#     current_user.involved_projects.append(current_project)
#     current_project.users.append(current_user)
#     db.session.add(current_user)
#     db.session.add(current_project)
#     # 2 Add user's entry in the project's resource table
#     new_member = dict['model_name'](id=320221138, Jan=15)
#     # 3* Fill user's resource data of each month in the table
#     return render_template('user/my_projects.html')
#
#
# def create_resource_table(project_id, project_name):
#     table_name = get_resource_table_name(project_id)
#     columns = {
#         "__tablename__": table_name,
#         "id": db.Column(db.Integer, primary_key=True, autoincrement=False),
#         "Year": db.Column(db.Integer),
#         "Jan": db.Column(db.Integer),
#         "Feb": db.Column(db.Integer),
#         "Mar": db.Column(db.Integer),
#         "Apr": db.Column(db.Integer),
#         "May": db.Column(db.Integer),
#         "Jun": db.Column(db.Integer),
#         "Jul": db.Column(db.Integer),
#         "Aug": db.Column(db.Integer),
#         "Sep": db.Column(db.Integer),
#         "Oct": db.Column(db.Integer),
#         "Nov": db.Column(db.Integer),
#         "Dec": db.Column(db.Integer),
#     }
#     # 由于使用flask migrate 必须创建对应模型来创建表
#     new_model = type(project_name, (db.Model,), columns)
#     dict['model_name'] = project_name
#     db.create_all()
#     return table_name
#
# def get_resource_table_name(project_id):
#     return "project_resource_" + str(project_id)
