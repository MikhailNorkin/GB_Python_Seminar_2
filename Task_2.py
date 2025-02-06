'''
Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно

'''
def def_2_8_16(count,x):
    test = count
    text = ''
    while count > x-1:
        next_value = count % x
        if next_value == 10:
            text = 'a' + text
        elif next_value == 11:
            text = 'b' + text
        elif next_value == 12:
            text = 'c' + text
        elif next_value == 13:
            text = 'd' + text
        elif next_value == 14:
            text = 'e' + text
        elif next_value == 15:
            text = 'f' + text
        else:
            text = str(next_value) + text
        count = count // x
    else:
        text = str(count) + text
    print('Посчитано программой:', text)

    if x == 2:
        print('Проверка в ',x,'-ой ', ' системе ', bin(test))
    elif x == 8:
        print('Проверка в ', x, '-ой ', ' системе ', oct(test))
    elif x == 16:
        print('Проверка в ', x, '-ой ', ' системе ', hex(test))

def main():
    count = int(input('Введите целое число '))
    def_2_8_16(count, 2)
    def_2_8_16(count, 8)
    def_2_8_16(count, 16)

if __name__ == "__main__":
    main()
