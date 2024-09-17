from flask import Blueprint

employee_blueprint = Blueprint("employee", __name__, url_prefix="/employees")

from .routes import routes
