import os
from .phonebook import PhoneBook
from .notes import Notes
from .file_manager import FileManager


class AbstractMenu:
    def __init__(self):
        self.menu_items = []
        self.actions = []
        self.stop_menu = False
        self.message = ''

    def show_menu(self):
        while not self.stop_menu:
            os.system("clear")
            print(self.message)
            for i, text in enumerate(self.menu_items):
                print(f'{i + 1}.{text}')
            choice = input('> ')
            try:
                if len(self.menu_items) >= int(choice) > 0:
                    func = self.actions[int(choice) - 1]
                    func()
            except Exception:
                pass

    def stop(self):
        self.stop_menu = True


class MainMenu(AbstractMenu):
    def __init__(self):
        AbstractMenu.__init__(self)
        self.menu_items = ['Телефонная книга', 'Заметки', 'Файлы', 'Выход']
        self.phonebook = PhoneBookMenu()
        self.notesbook = NotesMenu()
        self.file_manager = FileManagerMenu()
        self.message = 'Привет! Я твой личный помощник! Выберите действие: '
        self.actions = [self.phonebook.show_menu, self.notesbook.show_menu, self.file_manager.show_menu, quit]


class PhoneBookMenu(AbstractMenu):
    def __init__(self):
        AbstractMenu.__init__(self)
        self.menu_items = ['Все контакты', 'Добавить контакт', 'Редактировать контакт', 'Удалить контакт', 'Напомнить о дне рождении', 'Поиск', 'Выход']
        self.phonebook = PhoneBook()
        self.message = 'Выберите действие:'
        self.actions = [self.phonebook.show_all_contacts, self.phonebook.add_contact, self.phonebook.update_contact,
                        self.phonebook.delete_contact, self.phonebook.birthday_notifier, self.phonebook.find_by_name,
                        self.stop]

    # def show_menu(self):
    #     while not self.stop_menu:
    #         os.system("clear")
    #         print('Выбери действие:')
    #         for i, text in enumerate(self.menu_items):
    #             print(f'{i+1}.{text}')
    #         choice = input('> ')
    #         self.switch_choice(choice)
    #
    # def switch_choice(self, choice):
    #     if choice == '1':
    #         self.phonebook.show_all_contacts()
    #     if choice == '2':
    #         self.phonebook.add_contact()
    #     if choice == '3':
    #         self.phonebook.update_contact()
    #     if choice == '4':
    #         self.phonebook.delete_contact()
    #     if choice == '5':
    #         self.phonebook.birthday_notifier()
    #     if choice == '6':
    #         self.phonebook.find_by_name()
    #     if choice == '7':
    #         self.stop_menu = True


class NotesMenu(AbstractMenu):
    def __init__(self):
        AbstractMenu.__init__(self)
        self.menu_items = ['Добавить заметку', 'Редактировать заметку', 'Удалить заметку', 'Сортировать заметки по тегам',
                           'Поиск по тегам', 'Поиск по названию', 'Выход']
        self.notes = Notes()
        self.message = 'Выберите действие:'
        self.actions = [self.notes.add_note, self.notes.update_note, self.notes.delete_note, self.notes.sort_by_tags,
                        self.notes.find_by_tags, self.notes.find_by_title, self.stop]

    # def show_menu(self):
    #     while not self.stop_menu:
    #         os.system("clear")
    #         print('Выбери действие:')
    #         for i, text in enumerate(self.menu_items):
    #             print(f'{i + 1}.{text}')
    #         choice = input('> ')
    #         self.switch_choice(choice)
    #
    # def switch_choice(self, choice):
    #     if choice == '1':
    #         self.notes.add_note()
    #     if choice == '2':
    #         self.notes.update_note()
    #     if choice == '3':
    #         self.notes.delete_note()
    #     if choice == '4':
    #         self.notes.sort_by_tags()
    #     if choice == '5':
    #         self.notes.find_by_tags()
    #     if choice == '6':
    #         self.notes.find_by_title()
    #     if choice == '7':
    #         self.stop_menu = True


class FileManagerMenu(AbstractMenu):
    def __init__(self):
        AbstractMenu.__init__(self)
        self.menu_items = ['Сортировать файлы в папке', 'Выход']
        self.file_manager = FileManager()
        self.message = 'Выберите действие:'
        self.actions = [self.file_manager.sort_files, self.stop]

    # def show_menu(self):
    #     while not self.stop_menu:
    #         os.system("clear")
    #         print('Выбери действие:')
    #         for i, text in enumerate(self.menu_items):
    #             print(f'{i + 1}.{text}')
    #         choice = input('> ')
    #         self.switch_choice(choice)
    #
    # def switch_choice(self, choice):
    #     if choice == '1':
    #         self.file_manager.sort_files()
    #     if choice == '2':
    #         self.stop_menu = True
