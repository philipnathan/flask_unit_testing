from ..repositories.EmployeesRepository import EmployeesRepository
from db import roles


class AllEmployeesServices:
    def __init__(self, repository: EmployeesRepository):
        self.repository = repository

    def get_all_employees(self):
        return self.repository.get_all()

    def add_employee(self, data):
        self.add_employee_checker(data)
        return self.repository.add_new(**data)

    def add_employee_checker(self, data):
        required_keys = {"role", "employee_detail", "schedule", "status"}
        required_employee_detail_keys = {"name", "email", "phone_number"}
        required_schedule_keys = {
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        }

        missing_keys = required_keys - set(data.keys())
        if missing_keys:
            raise ValueError(f"Missing key: {', '.join(missing_keys)}")

        missing_employee_detail_keys = required_employee_detail_keys - set(
            data["employee_detail"].keys()
        )
        if missing_employee_detail_keys:
            raise ValueError(f"Missing key: {", ".join(missing_employee_detail_keys)}.")

        missing_schedule_keys = required_schedule_keys - set(data["schedule"].keys())
        if missing_schedule_keys:
            raise ValueError(f"Missing keys: {", ".join(missing_schedule_keys)}.")
        
        if data.get("role").lower() not in [role.lower() for role in roles]:
            raise ValueError (f"Role '{data.get("role")}' does not exist.")
