from flask import Flask
from app.animal import animal_blueprint
from app.employee import employee_blueprint
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)

    app.register_blueprint(animal_blueprint)
    app.register_blueprint(employee_blueprint)

    return app


philip_app = create_app()
