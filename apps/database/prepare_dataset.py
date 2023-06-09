from apps import db
from apps.authentication.models import User, Project, Team, Role, Resource, UserToProject
from apps.database.query import *
from flask_login import login_required, current_user


# ------------------------------Chart------------------------------ #
# View 1 用户视角 - 自己参与各个Project的各月Resource / 自己在各个月份的各Project Resource
# Months for each project / Projects for each month
@login_required
def prepare_user_year_resource_chart(user_id, year):
    resource = query_resource_by_user_year(user_id, year)
    dimensions = ['Project', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    source = [dimensions]
    for each in resource:
        project = Project.query.filter_by(id=each.project_id).first().name
        row = [project, each.Jan, each.Feb, each.Mar, each.Apr, each.May, each.Jun,
               each.Jul, each.Aug, each.Sep, each.Oct, each.Nov, each.Dec]
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = None
        source.append(row)
    col_cnt = len(dimensions) - 1  # row name not included
    row_cnt = len(source) - 1  # column name not included
    dataset_size = (row_cnt, col_cnt)
    dataset = {
        'size': dataset_size,
        'dataframe': {
            'source': source
        }
    }
    return dataset

# View 2 PM视角 - 每个Project各个用户各个月份Resource / 每个Project各个月份内各个用户Resource
# Months for each project / Projects for each month
@login_required
def prepare_project_year_resource_chart(project_id, year):
    resource = query_resource_by_project_year(project_id, year)
    dimensions = ['User', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    source = [dimensions]
    for each in resource:
        user = User.query.filter_by(id=each.user_id).first().username
        row = [user, each.Jan, each.Feb, each.Mar, each.Apr, each.May, each.Jun,
               each.Jul, each.Aug, each.Sep, each.Oct, each.Nov, each.Dec]
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = None
        source.append(row)
    col_cnt = len(dimensions) - 1  # row name not included
    row_cnt = len(source) - 1  # column name not included
    dataset_size = (row_cnt, col_cnt)
    dataset = {
        'size': dataset_size,
        'dataframe': {
            'source': source
        }
    }
    return dataset


# ------------------------------Chart End------------------------------ #
# project list - prepare each page
@login_required
def prepare_allProjectListByPage_Table(page, per_page):
    dimensions = ['id', 'name', 'product', 'priority', 'PM', 'status']
    source = [dimensions]
    table_rows = get_all_project_info_by_page(page, per_page)
    print(table_rows)
    for each_row in table_rows:
        source.append(each_row)
    col_cnt = len(dimensions)
    row_cnt = len(source) - 1  # column name not included
    dataset_size = (row_cnt, col_cnt)
    dataset = {
        'size': dataset_size,
        'dataframe': {
            'source': source
        }
    }
    return dataset


# project list - prepare each row in a page
@login_required
def get_all_project_info_by_page(page, per_page):
    projects = get_all_project_by_page(page, per_page)
    projects_info_dataset = []
    for project in projects:
        project_id = project.id
        project_name = project.name
        product = query_product_by_id(project.product_id).name
        priority = query_priority_by_id(project.priority_id).name
        pm_id = project.manager_id
        pm = query_user_by_id(project.manager_id).username
        status = query_status_by_id(project.status_id).name
        row = [project_id, project_name, product, priority, pm_id, pm, status]
        projects_info_dataset.append(row)
    return projects_info_dataset
