import re
from Person import Person


class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__id = kwargs.get('id')
        self.__email = kwargs.get('email')
        self.work_mood = kwargs.setdefault('work_mood', '')
        self.salary = kwargs.setdefault('salary', 1000)
        self.__is_manager = kwargs.setdefault('is_manager', False)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, employee_id):
        self.__id = employee_id

    @property
    def is_manager(self):
        return self.__is_manager

    @is_manager.setter
    def is_manager(self, employee_is_manager):
        self.__is_manager = employee_is_manager

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, employee_email):
        if re.fullmatch(r'\b[A-Za-z\d._%+-]+@[A-Za-z\d.-]+\.[A-Z|a-z]{2,}\b', employee_email):
            self.__email = employee_email
        else:
            pass

    def work(self, hours):
        if hours == 8:
            self.work_mood = 'happy'
        elif hours < 8:
            self.work_mood = 'tired'
        else:
            self.work_mood = 'lazy'

    def send_email(self, to, subject, body, receiver_name):
        file = open(f"email_from_{self.__id}_to_{receiver_name}.txt")
        file.write(f'From: {self.__email}\n')
        file.write(f'To: {to}\n')
        file.write(f'Subject: {subject}\n')
        file.write(f'{body}')
        file.close()

