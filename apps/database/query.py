from apps import db
from apps.authentication.models import User, Project, Team, Role, Resource, UserToProject
from flask_login import login_required, current_user


# ------------------------------Basic------------------------------ #

# ------------------------------Basic End------------------------------ #

# ------------------------------Project------------------------------ #

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


# ------------------------------Project End------------------------------ #


# ------------------------------Resource------------------------------ #

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


#  return a Resource record
def query_resource_by_user_project_year(user_id, project_id, year):
    resource = Resource.query.filter_by(user_id=user_id, project_id=project_id, year=year).first()
    return resource


# ------------------------------Resource End------------------------------ #

# ------------------------------Chart End------------------------------ #
@login_required
def prepare_resource_table_data_user(user_id):
    # 1 project_list[project_dict_1, project_dict_2, project_dict_3]
    # 2 project_dict{"name": …, "record_list": [record1, record_2, record_3]}
    # 3 cur_record{"year":…, "Jan":…, ………}

    # 1 project_list[project_dict_1, project_dict_2, project_dict_3]
    project_list = []
    projects = query_projects_by_user(user_id)
    for each in projects:
        # 2 project_dict{"name": ……, "record_list": [record1, record_2, record_3]}
        project_name = each.name
        record_list = []
        records = query_resource_by_user_project(user_id, each.id)
        for each in records:
            # 3
            # project_name = Project.query.filter_by(id=each.project_id).first().name
            # username = User.query.filter_by(id=each.user_id).first().username
            # resource_record = query_resource_record_user_project(user_id, each)
            cur_record = {
                # "user": username
                # "project": project_name,
                "year": each.year,
                "Jan": each.Jan,
                "Feb": each.Feb,
                "Mar": each.Mar,
                "Apr": each.Apr,
                "May": each.May,
                "Jun": each.Jun,
                "Jul": each.Jul,
                "Aug": each.Aug,
                "Sep": each.Sep,
                "Oct": each.Oct,
                "Nov": each.Nov,
                "Dec": each.Dec
            }
            record_list.append(cur_record)
        project_dict = {'name': project_name,
                        'data': record_list}
        project_list.append(project_dict)
    resource_data = project_list
    return resource_data


# return list of dict
# 1 user_year_resources [project_dict_1, project_dict_2, project_dict_3]
# 2 project_dict {"name": …, "data": [5, 10, ……(12 in total)]}
# 3 data [5, 10, ……(12 in total)]
@login_required
def query_resource_by_user_year_2(user_id, year):
    user_year_resources = []
    user_projects = query_projects_by_user(user_id)
    for each in user_projects:
        record = query_resource_by_user_project_year(user_id, each.id, year)
        project_dict = {'name': each.name,
                        'data': [record.Jan, record.Feb, record.Mar, record.Apr, record.May, record.Jun,
                                 record.Jul, record.Aug, record.Sep, record.Oct, record.Nov, record.Dec]
                        }
        user_year_resources.append(project_dict)
    chart_data = user_year_resources
    return chart_data


# return list of dict
# e.g. [{'name': 'Rubicon 2.0', 'data': 15}, {'name': 'Intrepid NMPA', 'data': 20}]
@login_required
def query_resource_by_user_month(user_id, year, month):
    personal_resource_this_year = query_resource_by_user_year_2(user_id, year)
    for each in personal_resource_this_year:
        # Use the data of the specific month to replace the list of the data of all months
        each["data"] = each["data"][month - 1]
    personal_resource_this_month = sorted(personal_resource_this_year, key=lambda x: x['data'], reverse=True)
    return personal_resource_this_month


# return list of list, sorted by value in descending order
# e.g. [['Intrepid NMPA', 'Rubicon 2.0'], [20, 15]]
@login_required
def query_resource_by_user_month_list(user_id, year, month):
    personal_resource_this_month = query_resource_by_user_month(user_id, year, month)
    # ['Intrepid NMPA', 'Rubicon 2.0']
    name_list = [each['name'] for each in personal_resource_this_month]
    # [20, 15]
    data_list = [each['data'] for each in personal_resource_this_month]
    personal_resource_this_month_list = [name_list, data_list]
    return personal_resource_this_month_list


# return int
@login_required
def query_total_resource_by_user_month(user_id, year, month):
    user_resource_month = query_resource_by_user_month(user_id, year, month)
    total_resource_month = 0
    for each in user_resource_month:
        total_resource_month = total_resource_month + each['data']
    return total_resource_month


# return ECharts Dataset
# e.g.
# dataset: {
#     source: [
#       ['product', '2015', '2016', '2017'],
#       ['Matcha Latte', 43.3, 85.8, 93.7],
#       ['Milk Tea', 83.1, 73.4, 55.1],
#       ['Cheese Cocoa', 86.4, 65.2, 82.5],
#       ['Walnut Brownie', 72.4, 53.9, 39.1]
#     ]
#   }
# @login_required
# def prepare_resource_dataset_by_user_year(user_id, year):
#     user_resource_month = query_resource_by_user_month(user_id, year)
#     total_resource_month = 0
#     for each in user_resource_month:
#         total_resource_month = total_resource_month + each['data']
#     return total_resource_month
