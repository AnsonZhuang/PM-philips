# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json

from apps import db
from apps.authentication.models import Resource
from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.database.query import query_user_by_id, get_all_projects_count, query_project_by_id
from apps.database.prepare_dataset import prepare_user_year_resource_chart, prepare_project_year_resource_barchart, \
    prepare_allProjectListByPage_Table, prepare_project_cards, prepare_project_year_resource_table, \
    prepare_project_year_resource_piechart
from datetime import date


# ============================= My Functions Start =============================

@blueprint.route('/index')
@login_required
def index():
    user_id = 1001
    year = 2023

    dataset = prepare_user_year_resource_chart(user_id, year)
    username = query_user_by_id(user_id).username

    datadict = {
        'user_id': user_id,
        'username': username,
        'year': year
    }

    # Pass a parameter as the reference for the width/height
    # of the <div> label containing the chart depending on
    # the number of the item
    return render_template('pages/index_demo.html', dataset=dataset, datadict=datadict)


@blueprint.route('/project_list')
@login_required
def project_list():
    search_str = request.args.get('search_str', 'default', type=str)
    # 显示全部
    if search_str == 'default':
        # 当前选中页面
        page = request.args.get('page', 1, type=int)
        # 10 results per page
        per_page = 10
        # table每行n等分
        n_fold = 1
        # 得到结果总数用于计算页数
        total_rows = get_all_projects_count()
        total_pages = total_rows // per_page + 1
        # 显示全部
        dataset = prepare_allProjectListByPage_Table(page, per_page)

        # row = [project_id, project_name, product, priority, pm_id, pm, status]
        datalabel = dataset['dataframe']['source'][0]
        dataframe = dataset['dataframe']['source'][1:]

        # 每页显示的数据量
        # 根据当前页和每页显示的数据量进行切割
        data_slice = dataframe

        return render_template('my_pages/project_list.html', project_label=datalabel,
                               project_list=data_slice, page=page, total_pages=total_pages, n_fold=n_fold,
                               search_str=search_str)
    # TODO Search for projects with keywords
    # else:
    #     # 当前选中页面
    #     page = request.args.get('page', 1, type=int)
    #     per_page = 2
    #     # table每行n等分
    #     n_fold = 1
    #     # 得到结果总数用于计算页数
    #     total_rows = get_search_projects_count(search_str)
    #     total_pages = total_rows // per_page + 1
    #     # 显示全部
    #     dataset = prepare_searchProjectListByPage_Table(search_str, page, per_page)
    #
    #     datalabel = dataset['dataframe']['source'][0]
    #     dataframe = dataset['dataframe']['source'][1:]
    #
    #     # 每页显示的数据量
    #     # 根据当前页和每页显示的数据量进行切割
    #     data_slice = dataframe
    #
    #     return render_template('pages/project_list.html', car_model_label=datalabel,
    #                            car_model_list=data_slice, page=page, total_pages=total_pages, n_fold=n_fold,
    #                            search_str=search_str)
    #


@blueprint.route('/project_resource_page')
@login_required
def project_resource_page():
    id = request.args.get('id', -1, type=int)
    if id == -1:
        return redirect(url_for("home_blueprint.project_list"))
    else:
        # TODO Render serveral charts to display information of the chosen project
        project_id = id
        project_name = query_project_by_id(project_id).name
        year = 2023

        # 渲染card数据
        card_datadict = prepare_project_cards(id)

        # 渲染barchart数据
        chart_dataset = prepare_project_year_resource_barchart(project_id, year)
        # 渲染piechart数据
        chart_dataset_2 = prepare_project_year_resource_piechart(project_id, year)

        chart_datadict = {
            'project_id': project_id,
            'project_name': project_name,
            'year': year
        }

        selection_text = {
            "member_months_bar": "Each Member-Months(Bar)",
            "member_months_pie": "Each Member-Months(Pie)",
            "month_members_bar": "Each Month-Members(Bar)",
            "month_members_pie": "Each Month-Members(Pie)",
        }



        # 渲染table数据
        table_dataset = prepare_project_year_resource_table(project_id, year)
        table_datalabel = table_dataset['dataframe']['source'][0]
        table_dataframe = table_dataset['dataframe']['source'][1:]
        table_datadict = {
            'project_id': project_id,
            'project_name': project_name,
            'year': year
        }

        # Pass a parameter as the reference for the width/height
        # of the <div> label containing the chart depending on
        # the number of the item
        return render_template('my_pages/project_resource_page.html',
                               card_datadict=card_datadict, chart_dataset=chart_dataset, chart_dataset_2=chart_dataset_2,
                               chart_datadict=chart_datadict, selection_text=selection_text,
                               table_dataset=table_dataset, table_datalabel=table_datalabel,
                               table_dataframe=table_dataframe, table_datadict=table_datadict)


@blueprint.route('/user_resource_page')
@login_required
def user_resource_page():
    id = request.args.get('id', -1, type=int)
    if id == -1:
        # TODO 后续用用户列表取代
        return redirect(url_for("home_blueprint.project_list"))
    else:
        # TODO Render serveral charts to display information of the chosen user
        user_id = id
        year = 2023
        dataset = prepare_user_year_resource_chart(user_id, year)
        username = query_user_by_id(user_id).username
        print(dataset)
        datadict = {
            'user_id': user_id,
            'username': username,
            'year': year
        }
        return render_template('my_pages/user_resource_page.html', dataset=dataset, datadict=datadict)


@blueprint.route("/update-project-resource", methods=['POST'])
@login_required
def update_project_resource():
    # role = g.access.role
    # admin权限
    if request.method == 'POST':
        data = json.loads(request.get_data())
        print(data)
        # For query
        user_id = data['user_id']
        project_id = data['project_id']
        year = data['year']
        resource = Resource.query.filter_by(user_id=user_id, project_id=project_id, year=year).first()
        resource.Jan = data['Jan']
        resource.Feb = data['Feb']
        resource.Mar = data['Mar']
        resource.Apr = data['Apr']
        resource.May = data['May']
        resource.Jun = data['Jun']
        resource.Jul = data['Jul']
        resource.Aug = data['Aug']
        resource.Sep = data['Sep']
        resource.Oct = data['Oct']
        resource.Nov = data['Nov']
        resource.Dec = data['Dec']
        db.session.commit()
        cur_resource = Resource.query.filter_by(user_id=user_id, project_id=project_id, year=year).first()
        print(cur_resource)
        return "update project resource"


# ============================= My Functions End =============================

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
