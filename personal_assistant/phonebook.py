import os
import re
import json
import time
from datetime import date
from .helpers import input_with_prefill

PhoneBookPath = "contacts.json"


class PhoneBook:
    def __init__(self):
        self.phonebook = []
        self.load_data()

    def load_data(self):
        if not os.path.isfile(PhoneBookPath):
            return None
        with open(PhoneBookPath) as json_file:
            self.phonebook = json.load(json_file)

    def save_data(self):
        with open(PhoneBookPath, "w") as outfile:
            json.dump(self.phonebook, outfile)

    def show_all_contacts(self):
        if self.print_contacts(self.phonebook):
            input('\nНажмите Enter для выхода')
        else:
            time.sleep(3)

    def print_contacts(self, contacts):
        os.system("clear")
        if not contacts:
            print('Контактов не найдено')
            return False
        for i, item in enumerate(contacts):
            self.print_one_contact(i, item)
        return True

    def print_one_contact(self, i, item):
        print('{0}.{1},\t{2},\t{3}/{4}/{5},\t{6},\t{7}'.format(i + 1, item['name'], item['address'],
                                                               item['date_of_birth']['day'],
                                                               item['date_of_birth']['month'],
                                                               item['date_of_birth']['year'], item['phone'],
                                                               item['email']))

    def is_exist_contact(self, id):
        if len(self.phonebook) >= id > 0:
            return True
        print('Контакта с такий порядковым номером не существует')
        return False

    def check_int_input(self, id):
        try:
            int(id)
            return True
        except ValueError:
            print('Неверный ввод')
            return False

    def add_contact(self):
        os.system("clear")
        contact = {}
        contact['date_of_birth'] = {}
        contact['name'] = input('Введите имя: ')
        contact['address'] = input('Введите адрес: ')
        contact['date_of_birth']['year'] = input('Введите год рождения: ')
        contact['date_of_birth']['month'] = input('Введите месяц рождения: ')
        contact['date_of_birth']['day'] = input('Введите день рождения: ')
        flag = False
        while not flag:
            contact['phone'] = input('Введите номер телефона: ')
            if len(contact['phone']) == 0:
                break
            flag = self.verify_phone(contact['phone'])
        flag = False
        while not flag:
            contact['email'] = input('Введите email: ')
            if len(contact['email']) == 0:
                break
            flag = self.verify_email(contact['email'])
        self.phonebook.append(contact)
        self.save_data()
        print('Контакт сохранен!')
        time.sleep(2)

    def verify_phone(self, phone):
        regex = re.compile(r'[\d]{10}')
        if not regex.match(phone):
            print("Неверный формат номера мобильного телефона")
            return False
        return True

    def verify_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            print("Неверный формат email")
            return False
        return True

    def delete_contact(self):
        if self.print_contacts(self.phonebook):
            to_delete = input('Введите порядковый номер контакта, который вы хотите удалить: ')
            if self.check_int_input(to_delete):
                if self.is_exist_contact(int(to_delete)):
                    del self.phonebook[int(to_delete)-1]
                    self.save_data()
                    print('Контакт удален.')
        time.sleep(2)

    def update_contact(self):
        if self.print_contacts(self.phonebook):
            flag = True
            while flag:
                to_update = input('Введите порядковый номер контакта, который вы хотите изменить(для отмены введите #): ')
                if to_update == '#':
                    flag = False
                    continue
                if self.check_int_input(to_update):
                    if self.is_exist_contact(int(to_update)):
                        flag = False
                        self.update(int(to_update))
        time.sleep(2)

    def update(self, id):
        to_update = self.phonebook[id-1]
        print('Введите новую информацию о контакте или нажмите Enter, чтобы оставить оригинальную.')
        to_update['name'] = input_with_prefill('Введите новое имя: ', to_update['name'])
        flag = False
        while not flag:
            phone = input_with_prefill('Введите новый номер телефона: ', to_update['phone'])
            flag = self.verify_phone(phone)
            if flag:
                to_update['phone'] = phone
        to_update['address'] = input_with_prefill('Введите новый адрес: ', to_update['address'])
        print('Введите новую дату рождения')
        to_update['date_of_birth']['year'] = input_with_prefill('Введите год: ', to_update['date_of_birth']['year'])
        to_update['date_of_birth']['month'] = input_with_prefill('Введите месяц: ', to_update['date_of_birth']['month'])
        to_update['date_of_birth']['day'] = input_with_prefill('Введите день: ', to_update['date_of_birth']['day'])
        flag = False
        while not flag:
            email = input_with_prefill('Введите новый email: ', to_update['email'])
            flag = self.verify_email(email)
            if flag:
                to_update['email'] = email
        self.save_data()
        print('Контакт изменен')

    def birthday_notifier(self):
        os.system("clear")
        if self.phonebook:
            flag = True
            while flag:
                days = input('Введите количество дней(для отмены введите #): ')
                if days == '#':
                    flag = False
                    continue
                if self.check_int_input(days):
                    flag = False
                    current_date = date.today()
                    contacts = []
                    for item in self.phonebook:
                        if int(item['date_of_birth']['month']) == current_date.month and int(item['date_of_birth']['day']) == current_date.day + int(days):
                            contacts.append(item)
                    self.print_contacts(contacts)
        input()

    def find_by_name(self):
        os.system("clear")
        print('Поиск по имени')
        name = input('Введите имя контакта(для отмены введите #): ')
        if name == '#':
            return
        contacts = []
        for item in self.phonebook:
            if name in item['name']:
                contacts.append(item)
        self.print_contacts(contacts)
        input()
