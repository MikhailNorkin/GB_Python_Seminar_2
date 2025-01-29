'''
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''

import sys

data = [11, -11, '111', 11]
result = []
result_one = []
for i, item in enumerate(data, start= 1):
    print(i)
    print(item)
    print(id(item))
    print(sys.getsizeof(item))
    print(hash(item))
    if isinstance(item,int) == True:
        if item > 0:
            print('Значение - положительное целое число!')
    if isinstance(item, str) == True:
        print('Значение - строка!')
    if item in result:
        result_one.append(item)
    result.append(item)
    print()

print(result_one)