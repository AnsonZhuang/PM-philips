# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

# # 用户账号基本信息 ID用户名邮箱密码时间team
# class User(db.Model):
#     __tablename__ = "user"
#     ID = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False, unique=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(200), nullable=False)
#     join_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
#     team = db.Column(db.String(50), nullable=False)
#
#     projects = db.relationship('Project', secondary=User_To_Project_Table, backref='members')
#
#     # team_short = db.Column(db.VARCHAR(10), db.ForeignKey('team.short_name'), nullable=False)
#     # team = db.relationship("Team", foreign_keys=team_short, backref="members")
#
#     def __repr__(self):
#         return "User:{}".format(str(self.name))
#
class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

# from exts import db
# from datetime import datetime
#
# User_To_Project_Table = db.Table('user_to_project', db.metadata,
#                                  db.Column('user_ID', db.Integer, db.ForeignKey('user.ID')),
#                                  db.Column('project_ID', db.Integer, db.ForeignKey('project.ID'))
#                                  )
#
#
# # 用户账号基本信息 ID用户名邮箱密码时间team
# class User(db.Model):
#     __tablename__ = "user"
#     ID = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False, unique=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(200), nullable=False)
#     join_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
#     team = db.Column(db.String(50), nullable=False)
#
#     projects = db.relationship('Project', secondary=User_To_Project_Table, backref='members')
#
#     # team_short = db.Column(db.VARCHAR(10), db.ForeignKey('team.short_name'), nullable=False)
#     # team = db.relationship("Team", foreign_keys=team_short, backref="members")
#
#     def __repr__(self):
#         return "User:{}".format(str(self.name))
#
#
# # 系统中录入了哪些组
# class Team(db.Model):
#     __tablename__ = "team"
#     ID = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     short_name = db.Column(db.VARCHAR(6), nullable=False, unique=True)
#     btn_name = db.Column(db.VARCHAR(10), nullable=False)
#     full_name = db.Column(db.VARCHAR(50), nullable=False, unique=True)
#
#     def __repr__(self):
#         return "Team:{}".format(str(self.short_name))
#
#
# class Role(db.Model):
#     __tablename__ = "role"
#     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.VARCHAR(30), nullable=False, unique=True)
#
#     def __repr__(self):
#         return "Role:{}".format(str(self.name))
#
#
# class Project(db.Model):
#     __tablename__ = "project"
#     ID = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     name = db.Column(db.VARCHAR(30), nullable=False, unique=True)
#     active = db.Column(db.Boolean, nullable=False)
#     users = db.relationship('User', secondary=User_To_Project_Table, backref='working_projects')
#
#     def __repr__(self):
#         return "Project:{}".format(str(self.name))
#
#
# class EmailCaptchaModel(db.Model):
#     __tablename__ = "email_captcha"
#     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     captcha = db.Column(db.String(10), nullable=False)
#     create_time = db.Column(db.DateTime, default=datetime.now)
#
#     def __repr__(self):
#         return "Name:{}, Count:{}".format(self.name, str(self.count))
#
#
# class UserAccess(db.Model):
#     __tablename__ = "user_access"
#     # 向账号表建立外键
#     ID = db.Column(db.Integer, db.ForeignKey('user.ID'), primary_key=True)
#     ID_backref = db.relationship("User", foreign_keys=ID, backref="user_access")
#     # staff 员工 manager 经理
#     role = db.Column(db.String(10), nullable=False)
#     # access = 0 staff（查看操作自己） 1 manager(查看操作Team, 建立Project) 2 director(查看操作所有人, 建立Project)
#     # True/False
#     access_ALL = db.Column(db.Boolean, nullable=False)
#     access_RD = db.Column(db.Boolean, nullable=False)
#     access_PMO = db.Column(db.Boolean, nullable=False)
#     access_SW = db.Column(db.Boolean, nullable=False)
#     access_VV = db.Column(db.Boolean, nullable=False)
#     access_SYS = db.Column(db.Boolean, nullable=False)
#     access_HW = db.Column(db.Boolean, nullable=False)
#     manage_ALL = db.Column(db.Boolean, nullable=False)
#     manage_RD = db.Column(db.Boolean, nullable=False)
#     manage_PMO = db.Column(db.Boolean, nullable=False)
#     manage_SW = db.Column(db.Boolean, nullable=False)
#     manage_VV = db.Column(db.Boolean, nullable=False)
#     manage_SYS = db.Column(db.Boolean, nullable=False)
#     manage_HW = db.Column(db.Boolean, nullable=False)
#     config_ALL = db.Column(db.Boolean, nullable=False)
#     config_RD = db.Column(db.Boolean, nullable=False)
#     config_PMO = db.Column(db.Boolean, nullable=False)
#     config_SW = db.Column(db.Boolean, nullable=False)
#     config_VV = db.Column(db.Boolean, nullable=False)
#     config_SYS = db.Column(db.Boolean, nullable=False)
#     config_HW = db.Column(db.Boolean, nullable=False)
#
#     def __repr__(self):
#         return "UserAccess:{}".format(str(self.name))
