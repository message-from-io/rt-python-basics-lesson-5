
'''
5.1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py). В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код. Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.
'''

import os, time

for i in range(1, 10):
    mkdirname = 'dir_{}'.format(i)
    os.mkdir(mkdirname)
mkdirlist = os.listdir(os.getcwd())
print('Создано {} каталогов: {}'.format(i, mkdirlist))

time.sleep(1)

for i in range(1, 10):
    rmdirname = 'dir_{}'.format(i)
    os.rmdir(rmdirname)
rmdirlist = os.listdir(os.getcwd())
print('Удалено {} каталогов: {}'.format(i, rmdirlist))

# Результат:
#
# Создано 9 каталогов: ['.idea', 'dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'Lesson_5_1.py']
# Удалено 9 каталогов: ['.idea', 'Lesson_5_1.py']
