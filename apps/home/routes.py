# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.database.query import query_total_resource_by_user_month, query_resource_by_user_year_2, \
    query_resource_by_user_month_list
from apps.database.prepare_dataset import prepare_resource_by_user_year
from datetime import date


@blueprint.route('/index')
@login_required
def index():
    cur_date = date.today()
    cur_year = cur_date.year
    cur_month = cur_date.month
    cur_day = cur_date.day

    # personal_resource_this_year[project_dict_1, project_dict_2, project_dict_3]
    # project_dict{"name": abc, "data": [5, 10, ……(12 in total)]}
    # data[5, 10, ……(12 in total)]
    personal_resource_this_year = query_resource_by_user_year_2(current_user.id, cur_year)

    # The user resource to each project this month in lists
    # e.g. [['Intrepid NMPA', 'Rubicon 2.0'], [20, 15]]
    personal_resource_this_month = query_resource_by_user_month_list(current_user.id, cur_year, cur_month)
    personal_resource_this_month = {'labels': personal_resource_this_month[0],
                                    'series': personal_resource_this_month[1]}

    # All user resource to projects this month
    total_personal_resource_this_month = query_total_resource_by_user_month(current_user.id, cur_year, cur_month)

    return render_template('pages/index.html', segment='index',
                           personal_resource_this_year=personal_resource_this_year,
                           personal_resource_this_month=personal_resource_this_month,
                           total_personal_resource_this_month=total_personal_resource_this_month)
    # total_personal_resource_this_month=temp_dict)


@blueprint.route('/index_demo')
@login_required
def index_demo():
    dataset = prepare_resource_by_user_year(320221138, 2023)
    print(dataset)
    return render_template('pages/index_demo.html', dataset=dataset)


@blueprint.route('/typography')
@login_required
def typography():
    return render_template('pages/typography.html')


@blueprint.route('/color')
@login_required
def color():
    return render_template('pages/color.html')


@blueprint.route('/icon-tabler')
@login_required
def icon_tabler():
    return render_template('pages/icon-tabler.html')


@blueprint.route('/sample-page')
@login_required
def sample_page():
    return render_template('pages/sample-page.html')


@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')


@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')


@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')


@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')


@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')


@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

# 在 Flask 中，你可以使用 Flask 的模板引擎来从 MySQL 数据库中获取数据，并将其渲染到 HTML 模板中，然后将数据作为 JavaScript 对象传递给你的 JS 文件。下面是一些基本步骤来完成这个任务：
#
# 从 MySQL 数据库中获取数据
# 使用 Flask 框架中的 SQLAlchemy 模块来连接到 MySQL 数据库，并编写查询语句从数据库中获取数据。例如：
# python
# Copy code
# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name'
# db = SQLAlchemy(app)
#
# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     value = db.Column(db.Integer)
#
# @app.route('/')
# def index():
#     data = Data.database.all()
#     return render_template('index.html', data=data)
#
#
# 渲染数据到 HTML 模板中
# 在 index() 函数中，我们将查询到的数据 data 传递给了模板引擎 render_template()。在 HTML 模板中，我们可以使用 Flask 的模板引擎语法将数据渲染到页面上，例如：
# html
# Copy code
# <div id="chart"></div>
#
# <script>
# var data = [
#     {% for item in data %}
#     {name: "{{ item.name }}", value: {{ item.value }}},
#     {% endfor %}
# ];
# </script>
# 这里我们将数据渲染到了一个 JavaScript 变量 data 中，该变量是一个包含多个对象的数组。每个对象都包含两个属性，即 name 和 value。
#
# 使用渲染后的数据更新图表
# 在 JS 文件中，你可以使用 data 变量来更新你的图表。例如，如果你正在使用 Chart.js 来绘制图表，可以这样做：
# javascript
# Copy code
# var ctx = document.getElementById('chart').getContext('2d');
# var chart = new Chart(ctx, {
#     type: 'bar',
#     data: {
#         labels: data.map(function(item) { return item.name }),
#         datasets: [{
#             label: 'My Dataset',
#             data: data.map(function(item) { return item.value }),
#             backgroundColor: 'rgba(255, 99, 132, 0.2)',
#             borderColor: 'rgba(255, 99, 132, 1)',
#             borderWidth: 1
#         }]
#     },
#     options: {
#         scales: {
#             y: {
#                 beginAtZero: true
#             }
#         }
#     }
# });
# 在这里，我们使用了 data 变量来设置图表的标签和数据。map() 方法将数据从包含对象的数组转换为包含值的数组。你可以根据需要调整这里的代码，以适应你自己的图表库。
#
# 总之，从 MySQL 数据库中获取数据，渲染到 HTML 模板中，再将数据传递给 JS 文件并使用它来更新图表是一种常见的方法，可以满足你的需求。
#
