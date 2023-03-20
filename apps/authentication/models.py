# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from datetime import datetime, date
from apps import db, login_manager
from apps.authentication.util import hash_pass

# multi-user - multi-project
# members of projects
# P.S. Sometimes we only assign projects to users, but not decide the lasting years of the projects
UserToProject = db.Table('user_to_project',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                         db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
                         )

# multi-project - multi-year
# Some project P is active in some year Y, i.e., in Y, some members of the project assign resource to
# the project, thus for each member M of the project, an entry E representing: the project resource of
# each month in Y assigned to P by M should be added to the table UserToYearOfProject.
# P.S. Sometimes we only decide the lasting years of the projects, but not assign projects to users
YearOfProject = db.Table('year_of_project',
                         # db.Column('project_year', db.Integer, primary_key=True),
                         db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
                         db.Column('year', db.Integer, primary_key=True)
                         )

# single-year_of_project - multi-user
# For a YearOfProject(Y-P) entry, each member of the P will have an entry in this table to display their
# resource assigned to P in Y
# UserToYearOfProject = db.Table('user_to_year_of_project',
#                                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#                                db.Column('project_id', db.Integer, db.ForeignKey('year_of_project.project_id'),
#                                          primary_key=True),
#                                db.Column('year', db.Integer, db.ForeignKey('year_of_project.year'), primary_key=True),
#                                db.Column('Jan', db.Integer),
#                                db.Column('Feb', db.Integer),
#                                db.Column('Mar', db.Integer),
#                                db.Column('Apr', db.Integer),
#                                db.Column('May', db.Integer),
#                                db.Column('Jun', db.Integer),
#                                db.Column('Jul', db.Integer),
#                                db.Column('Aug', db.Integer),
#                                db.Column('Sep', db.Integer),
#                                db.Column('Oct', db.Integer),
#                                db.Column('Nov', db.Integer),
#                                db.Column('Dec', db.Integer),
#                                )

# multi Manager - multi Team
ManagerToTeam = db.Table('manager_to_team', db.Column('manager_id', db.Integer, db.ForeignKey('user.id')),
                         db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
                         )


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    # e.g. 320221138
    id = db.Column(db.Integer, primary_key=True)
    # e.g. Anson Zhuang
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.LargeBinary, nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now, nullable=False)

    # e.g. employee/manager/director/admin
    # multi User - single Role
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    role = db.relationship('Role', uselist=False, foreign_keys='User.role_id', back_populates='users')

    # [some team]_[access/manage/config]
    # single User - single UserPermission
    user_permission = db.relationship('UserPermission', uselist=False, back_populates='user')

    # multi User - single Team
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    team = db.relationship('Team', uselist=False, foreign_keys='User.team_id', back_populates='users')

    # 用户管理的部门
    # multi Manager - multi Team
    managed_teams = db.relationship('Team', secondary=ManagerToTeam, back_populates='team_managers')

    # 用户参与的项目
    # multi User - multi Project
    involved_projects = db.relationship('Project', secondary=UserToProject, back_populates='users')

    # 用户创建的项目
    # single User - multi Project
    created_projects = db.relationship('Project', uselist=True, foreign_keys="Project.creator_id",
                                       back_populates='creator')

    # 用户管理的项目
    # single User - multi Project
    managed_projects = db.relationship('Project', uselist=True, foreign_keys="Project.manager_id",
                                       back_populates='manager')

    # 用户操作Project的日志
    project_operation_log = db.relationship('ProjectOperationLog', uselist=True, back_populates='user')

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


class Project(db.Model):
    __tablename__ = 'project'
    # Project's info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), nullable=False, unique=True)

    # [id] of e.g. A/B/C/D
    # multi Project - single Priority
    priority_id = db.Column(db.Integer, db.ForeignKey("project_priority.id"), nullable=False)
    priority = db.relationship("ProjectPriority", uselist=False, foreign_keys='Project.priority_id',
                               back_populates="projects")

    # e.g. [id] of DFM100
    # multi Project - single Product
    product_id = db.Column(db.Integer, db.ForeignKey("project_product.id"), nullable=False)
    product = db.relationship("ProjectProduct", uselist=False, foreign_keys='Project.product_id',
                              back_populates="projects")

    # Creator-项目创建者 # multi Project - single User = Creator
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    creator = db.relationship('User', uselist=False, foreign_keys='Project.creator_id',
                              back_populates='created_projects')

    # Manager-项目管理者 # multi Project - single User = Project Manager
    manager_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    manager = db.relationship('User', uselist=False, foreign_keys='Project.manager_id',
                              back_populates='managed_projects')

    # ==========项目相关时间==========
    # 项目在系统中被创建的时间
    create_date = db.Column(db.Date, default=date.today(), nullable=False)
    # 项目在系统中被关闭的时间 初始化时默认为创建时间
    status_update_date = db.Column(db.Date, default=date.today(), nullable=True)
    # 项目开始时间 仅为计划 用户自定义作为参考 在系统中没有实际影响
    launch_date = db.Column(db.Date, nullable=False)
    # 项目关闭时间 仅为计划 用户自定义作为参考 在系统中没有实际影响
    end_date = db.Column(db.Date, nullable=True)

    # ==========项目状态信息==========
    # True: 对所有成员visible False: 仅创建者可见
    visible = db.Column(db.Boolean, nullable=False)
    # Status-项目当前状态 # multi Project - single ProjectStatus
    status_id = db.Column(db.Integer, db.ForeignKey("project_status.id"), nullable=False)
    status = db.relationship("ProjectStatus", uselist=False, foreign_keys='Project.status_id',
                             back_populates="projects")
    # ==========项目具体信息==========
    # 项目具体内容
    description = db.Column(db.VARCHAR(500), nullable=True)
    # 项目具体计划
    plan = db.Column(db.VARCHAR(500), nullable=True)
    # 项目表名
    resource_table_name = db.Column(db.VARCHAR(100), nullable=True)
    # ==========非数据库字段 仅反向引用属性==========
    # multi Project - multi User
    users = db.relationship('User', secondary=UserToProject, back_populates='involved_projects')

    # Project的日志
    log = db.relationship('ProjectOperationLog', uselist=True, back_populates='project')

    def __repr__(self):
        return str(self.name)


class UserPermission(db.Model):
    __tablename__ = 'user_permission'
    # single User - single UserPermission
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', uselist=False, foreign_keys='UserPermission.id',
                           back_populates='user_permission')

    access_ALL = db.Column(db.Boolean, nullable=False)
    access_RD = db.Column(db.Boolean, nullable=False)
    access_PMO = db.Column(db.Boolean, nullable=False)
    access_SW = db.Column(db.Boolean, nullable=False)
    access_VV = db.Column(db.Boolean, nullable=False)
    access_SYS = db.Column(db.Boolean, nullable=False)
    access_HW = db.Column(db.Boolean, nullable=False)

    manage_ALL = db.Column(db.Boolean, nullable=False)
    manage_RD = db.Column(db.Boolean, nullable=False)
    manage_PMO = db.Column(db.Boolean, nullable=False)
    manage_SW = db.Column(db.Boolean, nullable=False)
    manage_VV = db.Column(db.Boolean, nullable=False)
    manage_SYS = db.Column(db.Boolean, nullable=False)
    manage_HW = db.Column(db.Boolean, nullable=False)

    config_ALL = db.Column(db.Boolean, nullable=False)
    config_RD = db.Column(db.Boolean, nullable=False)
    config_PMO = db.Column(db.Boolean, nullable=False)
    config_SW = db.Column(db.Boolean, nullable=False)
    config_VV = db.Column(db.Boolean, nullable=False)
    config_SYS = db.Column(db.Boolean, nullable=False)
    config_HW = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return 'UserAccess:{}'.format(str(self.name))


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(30), nullable=False, unique=True)

    # multi User vs single Role
    users = db.relationship('User', uselist=True, back_populates='role')

    def __repr__(self):
        return 'Role:{}'.format(str(self.name))


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  # e.g. 1
    full_name = db.Column(db.VARCHAR(50), nullable=False, unique=True)  # e.g. System Engineering
    short_name = db.Column(db.VARCHAR(10), nullable=False, unique=True)  # e.g. R&D
    pure_letter_name = db.Column(db.VARCHAR(10), nullable=False, unique=True)  # e.g. RD
    # multi Team vs multi manager
    team_managers = db.relationship('User', secondary=ManagerToTeam, back_populates='managed_teams')
    # single Team vs multi User
    users = db.relationship('User', uselist=True, back_populates='team')

    def __repr__(self):
        return 'Team:{}'.format(str(self.short_name))


class ProjectPriority(db.Model):
    __tablename__ = 'project_priority'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    # single Priority - multi Project
    name = db.Column(db.VARCHAR(20), nullable=False, unique=True)
    projects = db.relationship("Project", uselist=True, back_populates="priority")

    def __repr__(self):
        return 'Project Priority:{}'.format(str(self.name))


class ProjectProduct(db.Model):
    __tablename__ = 'project_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    # single Product - multi Project
    name = db.Column(db.VARCHAR(50), nullable=False)
    projects = db.relationship("Project", uselist=True, back_populates="product")

    def __repr__(self):
        return 'Project Product:{}'.format(str(self.name))


class ProjectStatus(db.Model):
    __tablename__ = 'project_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    # single ProjectStatus - multi Project
    name = db.Column(db.VARCHAR(50), nullable=False)
    projects = db.relationship("Project", uselist=True, back_populates="status")

    def __repr__(self):
        return 'Project Status:{}'.format(str(self.name))


class ProjectOperationLog(db.Model):
    __tablename__ = 'project_operation_log'
    # 暂定Log记录id生成策略为:共16位 前14位为 插入时的datetime(yyyy-mm-dd-hh-mm-ss)转换为14位纯数字 低2位从00开始 如重复则+1
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    # 发生时间
    log_time = db.Column(db.DateTime, nullable=False)
    # single log entry - a single user operating on a single project
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', uselist=False, foreign_keys='ProjectOperationLog.project_id',
                              back_populates='log')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', uselist=False, foreign_keys='ProjectOperationLog.user_id',
                           back_populates='project_operation_log')

    # 日志记录具体的项目操作文字描述
    entry = db.Column(db.VARCHAR(256), nullable=False)

    def __repr__(self):
        return 'Project Operation Log:{}'.format(str(self.name))


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
