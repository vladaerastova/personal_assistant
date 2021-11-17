import os


class FileManager:
    def __init__(self):
        self.extensions = [{'name': 'Документы', 'ext': ['.pdf', '.docx', '.doc', '.txt', 'odt'], 'files': []},
                           {'name': 'Изображения', 'ext': ['.jpeg', '.jpg', '.svg', '.png', '.PNG'], 'files': []},
                           {'name': 'Видео', 'ext': ['.mp4', '.mp3', '.avi'], 'files': []},
                           {'name': 'Установочные файлы', 'ext': ['.exe', '.msi'], 'files': []},
                           {'name': 'Сжатые файлы', 'ext': ['.zip'], 'files': []}]
        self.other = []

    def check_dir(self, dir):
        if not os.path.isdir(dir):
            print('Директория не существуеn')
            return False
        if not os.path.exists(dir):
            print('Директория не существует')
            return False
        if not os.access(dir, os.R_OK):
            print('Нет доступа')
            return False
        return True

    def sort_files(self):
        directory = input('Введите абсолютный путь к директории: ')
        if self.check_dir(directory):
            all_files = os.listdir(directory)
            for file in all_files:
                added = False
                for ext in self.extensions:
                    if os.path.splitext(file)[1] in ext['ext']:
                        ext['files'].append(file)
                        added = True
                if not added:
                    self.other.append(file)
            self.print_sorted_files()
        input()

    def print_sorted_files(self):
        os.system("clear")
        for item in self.extensions:
            if item['files']:
                print(item['name'])
                print(item['files'])
                print('\n')
        if self.other:
            print('Другое')
            print(self.other)
