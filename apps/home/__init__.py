# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint

blueprint = Blueprint('home_blueprint', __name__, url_prefix='')
user_bp = Blueprint("user", __name__, url_prefix="/user")