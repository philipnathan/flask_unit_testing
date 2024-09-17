from flask import request
from flasgger import swag_from

from .. import employee_blueprint
from ..services.AllEmployeeServices import AllEmployeesServices
from ..services.SpecificEmployeeServices import SpecificEmployeeServices
from ..repositories.EmployeesRepository import EmployeesRepository

all_employees_services = AllEmployeesServices(EmployeesRepository())
specific_emloyee_services = SpecificEmployeeServices(EmployeesRepository())


@employee_blueprint.route("/", methods=["GET"])
@swag_from("../docs/get_all_employees.yml")
def all_employee():
    return {"employee_data": all_employees_services.get_all_employees()}, 200


@employee_blueprint.route("/", methods=["POST"])
@swag_from("../docs/create_employee.yml")
def create_employee():
    try:
        data = request.get_json()
        result = all_employees_services.add_employee(data)
        return {
            "employee_data": result,
            "message": "New employee is successfully added.",
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 400


@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
@swag_from("../docs/get_specific_employee.yml")
def specific_employee(employee_id):
    try:
        return {
            "employee_data": specific_emloyee_services.get_specific_employee(
                employee_id
            )
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 400


@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
@swag_from("../docs/delete_specific_employee.yml")
def delete_employee(employee_id):
    try:
        specific_emloyee_services.delete_specific_employee(employee_id)
        return {"message": "Employee data is successfully deleted"}, 200
    except ValueError as e:
        return {"error": str(e)}, 400


@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
@swag_from("../docs/update_specific_employee.yml")
def update_employee(employee_id):
    try:
        data = request.get_json()
        result = specific_emloyee_services.edit_specific_employee(employee_id, data)
        return {
            "employee_data": result,
            "message": "Employee data is successfully updated",
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 400
