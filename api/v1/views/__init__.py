from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/app/v1")

from app.v1.views.index import *
