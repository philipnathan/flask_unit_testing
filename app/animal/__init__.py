from flask import Blueprint

animal_blueprint = Blueprint("animal", __name__, url_prefix="/animals")

from .routes import routes
