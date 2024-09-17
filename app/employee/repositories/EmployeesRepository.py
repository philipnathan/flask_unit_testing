from db import employees


class EmployeesRepository:
    def __init__(self):
        self.repository = employees

    def get_all(self):
        return self.repository

    def add_new(self, **data):
        employee_id = str(max(list(employees.keys())) + 1)
        new_employee = {employee_id: {}}

        for key, value in data.items():
            new_employee[employee_id][key] = value

        return new_employee

    def get_specific(self, employee_id):
        if employee_id not in self.repository:
            raise ValueError(f"Employee with ID {employee_id} is not exist.")

        return self.repository[employee_id]

    def delete_specific(self, employee_id):
        if employee_id not in self.repository:
            raise ValueError(f"Employee with ID {employee_id} is not exist.")

        del self.repository[employee_id]

    def edit_specific(self, employee_id, **kwargs):
        choosen_employee = self.repository[employee_id]

        self.nested_update(choosen_employee, kwargs)

        return choosen_employee

    def nested_update(self, current_data, incoming_data, parent_key=""):
        for key, value in incoming_data.items():
            if isinstance(value, dict):
                current_key = f"{parent_key}[key]" if parent_key else key
                self.nested_update(
                    current_data=current_data.get(key),
                    incoming_data=value,
                    parent_key=current_key,
                )
            else:
                current_data[key] = value
