from Employee import Employee
from Office import Office

office = Office('My_Office_1')

emp1 = Employee(full_name='Ramez', health_rate=100, id=1, email='ramez@gmail.com', salary=2000, is_manager=False)
emp2 = Employee(full_name='Aly', health_rate=50, id=2, email='aly@gmail.com', salary=5000, is_manager=True)


office.hire_employee(emp1)
office.hire_employee(emp2)

office.fire_employee(1)
