from apps import db
from apps.authentication.models import User, Project, ProjectProduct, Team, Role, Resource, UserToProject, \
    ProjectProduct, ProjectPriority, ProjectStatus
from flask_login import login_required, current_user


# ------------------------------Chart Start------------------------------ #

# ------------------------------Basic------------------------------ #
# return a User
def query_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


# return a list of User(s)
def query_users_by_ids(*user_ids):
    users = [User.query.filter_by(id=each_user_id) for each_user_id in user_ids]
    return users


def query_product_by_id(product_id):
    product = ProjectProduct.query.filter_by(id=product_id).first()
    return product



def query_priority_by_id(priority_id):
    priority = ProjectPriority.query.filter_by(id=priority_id).first()
    return priority


def query_status_by_id(status_id):
    status = ProjectStatus.query.filter_by(id=status_id).first()
    return status


# ------------------------------Basic End------------------------------ #

# ------------------------------Project------------------------------ #
# return a Project
def query_project_by_id(project_id):
    project = Project.query.filter_by(id=project_id).first()
    return project


# return a list of Project(s)
def query_projects_by_ids(*project_ids):
    projects = [Project.query.filter_by(id=each_project_id) for each_project_id in project_ids]


# return a list of Project(s)
def query_projects_all():
    projects = Project.query.all()
    return projects

# return a list of Project(s)
@login_required
def query_projects_by_user(user_id):
    query = db.session.query(UserToProject)
    project_ids = [each.project_id for each in query.filter_by(user_id=user_id).all()]
    user_projects = [Project.query.filter_by(id=each).first() for each in project_ids]
    return user_projects


# return a list of Project(s)
@login_required
def query_created_projects_by_user(user_id):
    created_projects = Project.query.filter_by(creator_id=user_id).all()
    return created_projects


# project list - prepare all project instances - with page params
# 用于分页返回Project列表结果
@login_required
def get_all_project_by_page(page, per_page):
    query = Project.query
    page_of_projects = query.paginate(page=page, per_page=per_page).items
    return page_of_projects


# ------------------------------Project End------------------------------ #

# ------------------------------Resource------------------------------ #
# Resource的1/2/3参数版本
# return a list of Resource record(s)
@login_required
def query_resource_by_user(user_id):
    resource_record = Resource.query.filter_by(user_id=user_id).all()
    return resource_record


# return a list of Resource record(s)
@login_required
def query_resource_by_project(project_id):
    resource_record = Resource.query.filter_by(project_id=project_id).all()
    return resource_record


# return a list of Resource record(s)
@login_required
def query_resource_by_year(year):
    resource_record = Resource.query.filter_by(year=year).all()
    return resource_record


# return a list of Resource record(s)
@login_required
def query_resource_by_user_project(user_id, project_id):
    resource_record = Resource.query.filter_by(user_id=user_id, project_id=project_id).all()
    return resource_record


# return a list of Resource record(s)
@login_required
def query_resource_by_user_year(user_id, year):
    resource_record = Resource.query.filter_by(user_id=user_id, year=year).all()
    return resource_record


# return a list of Resource record(s)
@login_required
def query_resource_by_project_year(project_id, year):
    resource_record = Resource.query.filter_by(project_id=project_id, year=year).all()
    return resource_record


#  return a Resource record (ONLY ONE)
def query_resource_by_user_project_year(user_id, project_id, year):
    resource = Resource.query.filter_by(user_id=user_id, project_id=project_id, year=year).first()
    return resource


# ------------------------------Resource End------------------------------ #

# ------------------------------Chart End------------------------------ #

# ------------------------------NEW START------------------------------ #
# return list of dict = project_dict {"name": …, "data": [5, 10, ……(12 in total)]}
# View 1.1 单用户-指定年份12月-所有项目
@login_required
def prepare_resource_by_user_year(user_id, year):
    user_year_resources = []
    # 1 用户的所有项目
    user_projects = query_projects_by_user(user_id)
    # 2 对于每个项目的各个月份
    for each in user_projects:
        record = query_resource_by_user_project_year(user_id, each.id, year)
        project_dict = {'name': each.name,
                        'data': [record.Jan, record.Feb, record.Mar, record.Apr, record.May, record.Jun,
                                 record.Jul, record.Aug, record.Sep, record.Oct, record.Nov, record.Dec]
                        }
        user_year_resources.append(project_dict)
    chart_data = user_year_resources
    return chart_data


# 返回Project对象总数
@login_required
def get_all_projects_count():
    return Project.query.count()
