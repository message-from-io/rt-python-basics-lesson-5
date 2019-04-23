
import random as rnd

def get_random_item(list):
    if len(list) == 0:
        # return None
       result = None
    else:
        random_item_number = rnd.randint(0, len(list) - 1)
        # return list[random_item_number]
        result = list[random_item_number]
    # Проверка работы функции
    print(result)
