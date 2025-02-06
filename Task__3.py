'''
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
'''

from math import pi
import decimal

def main():
    decimal.getcontext().prec = 48
    diameter = int(input('Введите диаметр круга '))
    PI = decimal.Decimal(pi)
    print('Длина круга будет равна ', decimal.Decimal(round(diameter * PI, 42 )))
    print('Площадь круга равна ', decimal.Decimal(round(PI * diameter**2 / 4,42)))

if __name__ == "__main__":
    main()

