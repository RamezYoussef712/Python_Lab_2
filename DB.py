import mysql.connector


class DB:
    def __init__(self, host, user, password, database):
        self.DB_connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.DB_connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY,
                            full_name VARCHAR(255),
                            money INTEGER,
                            sleep_mood VARCHAR(255),
                            health_rate INTEGER,
                            email VARCHAR(255),
                            work_mood VARCHAR(255),
                            salary INTEGER,
                            is_manager BOOLEAN
                            );
                            ''')
        self.DB_connection.commit()

    def add_employee(self, employee):
        self.cursor.execute('''
            INSERT INTO employees (id, full_name, money, sleep_mood, health_rate, email, work_mood, salary, is_manager)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (employee.__id, employee.__full_name, employee.__money, employee.__sleep_mood, employee.__health_rate,
              employee.__email, employee.__work_mood, employee.salary, employee.__is_manager))
        self.DB_connection.commit()

    def get_employee(self, employee_id):
        self.cursor.execute('''
            SELECT * FROM employees WHERE employee_id = %s
        ''', (employee_id,))
        employee = self.cursor.fetchone()
        return employee

    def get_employees(self):
        self.cursor.execute('''
            SELECT * FROM employees
        ''')
        employees = self.cursor.fetchall()
        return employees
    @classmethod
    def delete_employee(cls, employee_id):
        cls.cursor.execute('''
            DELETE FROM employees WHERE employee_id = %s
        ''', (employee_id,))
        self.DB_connection.commit()

    # @classmethod
    # def delete(cls, employee_id):
    #     cls.delete_employee(employee_id)

