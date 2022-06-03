from DB import DB


class Office:
    def __init__(self, name):
        self.name = name
        self.db = DB('localhost', 'root', '', 'iti')

    def get_all_employees(self):
        return self.db.get_employees()

    def get_employee(self, employee_id):
        return self.db.get_employee(employee_id)

    def hire_employee(self, employee):
        self.db.add_employee(employee)

    def fire_employee(self, employee_id):
        self.db.delete_employee(employee_id)
