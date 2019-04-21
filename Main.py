
'''
5.3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте, что все работает как надо.

Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
'''

import Lesson_5_1
from Module import get_random_item

list = []
get_random_item(list)

list = [1, 2, 3, 4]
get_random_item(list)

# Результат:
#
# Создано 9 каталогов: ['.idea', 'dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'Lesson_5_1.py', 'Lesson_5_2.py', 'Main.py', 'Module.py', '__pycache__']
# Удалено 9 каталогов: ['.idea', 'Lesson_5_1.py', 'Lesson_5_2.py', 'Main.py', 'Module.py', '__pycache__']
# None
# 2
