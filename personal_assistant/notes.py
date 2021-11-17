import os
import json
import time
from .helpers import input_with_prefill


NotesPath = "notes.json"


class Notes:
    def __init__(self):
        self.notes = []
        self.load_data()

    def load_data(self):
        if not os.path.isfile(NotesPath):
            return None
        with open(NotesPath) as json_file:
            self.notes = json.load(json_file)

    def save_data(self):
        with open(NotesPath, "w") as outfile:
            json.dump(self.notes, outfile)

    def print_one_note(self, i, item):
        text = item['body'][:30]+'...' if len(item['body']) > 30 else item['body']
        print('{0}.{1}\n{2}\nТеги: {3}'.format(i + 1, item['title'], text, item['tags']))

    def print_notes(self, notes):
        os.system("clear")
        if len(notes) == 0:
            print('Заметок не найдено!')
            return False
        for i, item in enumerate(notes):
            self.print_one_note(i, item)
            print('\n')
        return True

    def is_exist(self, id):
        if len(self.notes) >= id > 0:
            return True
        print('Заметки с такий порядковым номером не существует')
        return False

    def check_int_input(self, id):
        try:
            int(id)
            return True
        except ValueError:
            print('Неверный ввод')
            return False

    def add_note(self):
        os.system("clear")
        note = {}
        note['title'] = input('Введите заголовок: ')
        note['body'] = input('Введите текст: ')
        note['tags'] = [x.strip().lower() for x in input('Добавьте теги через запятую: ').split(',')]
        self.notes.append(note)
        self.save_data()
        print('Заметка создана!')
        time.sleep(2)

    def delete_note(self):
        if self.print_notes(self.notes):
            flag = True
            while flag:
                to_delete = input(
                    'Введите порядковый номер заметки, которую вы хотите удалить(для отмены введите #): ')
                if to_delete == '#':
                    flag = False
                    continue
                if self.check_int_input(to_delete):
                    if self.is_exist(int(to_delete)):
                        flag = False
                        del self.notes[int(to_delete) - 1]
                        self.save_data()
                        print('Заметка удалена.')
        time.sleep(2)

    def update_note(self):
        if self.print_notes(self.notes):
            flag = True
            while flag:
                to_update = input('Введите порядковый номер заметки, которую вы хотите изменить(для отмены введите #): ')
                if to_update == '#':
                    flag = False
                    continue
                if self.check_int_input(to_update):
                    if self.is_exist(int(to_update)):
                        flag = False
                        self.update(int(to_update))
        time.sleep(2)

    def update(self, id):
        os.system("clear")
        to_update = self.notes[id - 1]
        print('Введите новые данные или нажмите Enter, чтобы оставить оригинальные.')
        to_update['title'] = input_with_prefill('Измените заголовок: ', to_update['title'])
        to_update['body'] = input_with_prefill('Измените текст: ', to_update['body'])
        to_update['tags'] = [x.strip().lower() for x in input_with_prefill('Измените теги: ', ','.join(to_update['tags'])).split(',')]
        self.save_data()
        print('Заметка изменена')

    def find_by_title(self):
        os.system("clear")
        print('Поиск по заголовку')
        title = input('Введите текст(для отмены введите #): ')
        if title == '#':
            return
        notes = []
        for item in self.notes:
            if title in item['title']:
                notes.append(item)
        self.print_notes(notes)
        input()

    def find_by_tags(self):
        os.system("clear")
        print('Поиск по тегам')
        tags = [tag.strip().lower() for tag in input('Введите теги через запятую(для отмены введите #): ').split(',')]
        if tags[0] == '#':
            return
        notes = []
        for item in self.notes:
            if any(tag in item['tags'] for tag in tags):
                notes.append(item)
        self.print_notes(notes)
        input()

    def sort_by_tags(self):
        os.system("clear")
        all_tags = set([el for item in self.notes for el in item['tags']])
        for tag in all_tags:
            print('Тег #{0}'.format(tag))
            counter = -1
            for note in self.notes:
                if tag in note['tags']:
                    counter += 1
                    self.print_one_note(counter, note)
            print('\n')
        input()
