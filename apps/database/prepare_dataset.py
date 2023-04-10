from apps import db
from apps.authentication.models import User, Project, Team, Role, Resource, UserToProject
from apps.database.query import *
from flask_login import login_required, current_user


# ------------------------------Chart------------------------------ #

@login_required
def prepare_resource_by_user_year(user_id, year):
    resource = query_resource_by_user_year(user_id, year)
    dimensions = ['Project', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    source = []
    for each in resource:
        print(each)
        project = Project.query.filter_by(id=each.project_id).first().name
        row = {
            'Project': project,
            'Jan': each.Jan,
            'Feb': each.Feb,
            'Mar': each.Mar,
            'Apr': each.Apr,
            'May': each.May,
            'Jun': each.Jun,
            'Jul': each.Jul,
            'Aug': each.Aug,
            'Sep': each.Sep,
            'Oct': each.Oct,
            'Nov': each.Nov,
            'Dec': each.Dec,
        }
        for k, v in row.items():
            if v == 0:
                row[k] = None
        source.append(row)
        print(row)
    dataset = {
        'dimensions': dimensions,
        'source': source
    }
    return dataset

# dataset: {
#           // 用 dimensions 指定了维度的顺序。直角坐标系中，如果 X 轴 type 为 category，
#           // 默认把第一个维度映射到 X 轴上，后面维度映射到 Y 轴上。
#           // 如果不指定 dimensions，也可以通过指定 series.encode
#           // 完成映射，参见后文。
#           dimensions: ['product', 'Mon', 'Tue', 'Wed'],
#           source: [
#             { product: 'Matcha Latte', 'Mon': 43.3, 'Tue': 85.8, 'Wed': 93.7 },
#             { product: 'Milk Tea', 'Mon': 83.1, 'Tue': 73.4, 'Wed': 55.1 },
#             { product: 'Cheese Cocoa', 'Mon': 86.4, 'Tue': 65.2, 'Wed': 82.5 },
#             { product: 'Walnut Brownie', 'Mon': 72.4, 'Tue': 53.9, 'Wed': 39.1 }
#           ]
#         }
# ------------------------------Chart End------------------------------ #
