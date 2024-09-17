from ..repositories.EmployeesRepository import EmployeesRepository


class SpecificEmployeeServices:
    def __init__(self, repository: EmployeesRepository):
        self.repository = repository

    def get_specific_employee(self, employee_id):
        return self.repository.get_specific(employee_id)

    def delete_specific_employee(self, employee_id):
        return self.repository.delete_specific(employee_id)

    def edit_specific_employee(self, employee_id, data):
        required_keys = ["role", "employee_detail", "schedule", "status"]
        required_employee_detail_keys = ["name", "email", "phone_number"]
        required_schedule_keys = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]

        if not isinstance(data, dict):
            raise ValueError("Input data must be a JSON")
        if not data:
            raise ValueError("JSON Can not be empty")
        if data.get("employee_id"):
            raise ValueError("Please don't input employee ID directly in JSON")

        if data.get("employee_detail"):
            for key, value in data.get("employee_detail").items():
                if key not in required_employee_detail_keys:
                    raise ValueError(f"Please check your input '{key}' key")

        if data.get("schedule"):
            for key, value in data.get("schedule").items():
                if key not in required_schedule_keys:
                    raise ValueError(f"Please check your input '{key}' key")

        for key, value in data.items():
            if key not in required_keys:
                raise ValueError(f"Please check your input '{key}' key")

        return self.repository.edit_specific(employee_id, **data)
