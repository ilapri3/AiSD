class Phone_list():
    def __init__(self):
        self.entries = []

    def add_info(self, info):
        self.entries.append(info)
    
    def show_phone_list(self):
        return self.entries

    def search_surname(self, surname):
        for el in self.entries:
            if isinstance(el, Person) and el.surname == surname:
                el.show_info()


book = Phone_list()

class Person():
    def __init__(self, name, surname, address, phone_number):
        self.name  = name
        self.surname = surname
        self.address = address
        self.phone_number = phone_number
    
    def show_info(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Адрес: {self.address}, Телефонный номер: {self.phone_number}'
    
    def check_surname(self, surname):
        return self.surname == surname


human = Person('Ilya', 'Priemyshev', 'Moscow', '+7-(999)-999-99-99')

class Organization():
    def __init__(self, org_name, address, phone_number, fax, contact_person):
        self.org_name = org_name
        self.address = address
        self.phone_number = phone_number
        self.fax = fax
        self.conact_person = contact_person
    
    def show_info(self):
        return f'Название организации: {self.org_name}, Адрес: {self.address}, Телефонный номер: {self.phone_number}, Факс: {self.fax}, Контактное лицо{self.conact_person}'

    def check_surname(self, surname):
        return self.surname == surname


company = Organization('Progeek', 'Kazan', '+7-(999)-999-01-01', '999-99-99', 'Galiev')

class Friend():
    def __init__(self, name, surname, address, date_of_birth):
        self.name = name
        self.surname = surname
        self.address = address
        self.date_of_birth = date_of_birth

    def show_info(self):
        return f'Имя друга: {self.name}, Фамилия друга: {self.surname}, Адрес друга: {self.address}, Дата рождения друга: {self.date_of_birth}'

    def check_surname(self, surname):
        return self.surname == surname

    
buddy = Friend('Mark', 'Ivanov', 'Vladimir', '12-04-2001')

book.add_info(human.show_info())
book.add_info(company.show_info())
book.add_info(buddy.show_info())

print(book.show_phone_list())
print('')
find_surname = 'Priemyshev'
print(book.search_surname(find_surname))