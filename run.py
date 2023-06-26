# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from flask_migrate import Migrate
from flask_minify import Minify
from sys import exit
from apps.config import config_dict
from apps import create_app, db
from flask import g

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE')
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)

#
# @app.before_request
# def before_request():
#     # 从登录时创建的session中获取名为user_id的值，即user的id
#     user_id = session.get("user_id")
#     if user_id:
#         try:
#             g.user = User.query.get(user_id)
#             g.access = UserPermission.query.get(user_id)
#             g.user_id = user_id
#             g.role = Role.query.get(g.user.role_id).name
#             # setattr(g, "user", user)
#         except:
#             pass
#
#
# 上下文处理注解 - 渲染的所有模板都会执行这个函数 返回字典包含需要在模板中使用的全局变量
# TODO 如有需求可取消注释 用于各个模板中需要使用的全局变量
# @login required
# @app.context_processor
# def context_processor():
#     if hasattr(g, "user"):
#         # print(g.user.id)
#         # print(g.access.role)
#         return {"user": g.user,
#                 "user_id": g.user_id,
#                 "access": g.access,
#                 "role": g.role}
#     else:
#         return {}



if __name__ == "__main__":
    app.run()
