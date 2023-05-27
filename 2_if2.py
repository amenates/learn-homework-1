"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(first, second):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if isinstance(first, str) and isinstance(second, str):
        first = first.lower()
        second = second.lower()

        if first == second:
            print(1)
        elif first != second and len(first) > len(second):
            print(2)
        elif first != second and second == 'learn':
            print(3)
        else:
            print('Строки не равны')
    else:
        print(0)

if __name__ == "__main__":
    main('Hello', 'Learn')
    main('Hello', 'Hello')
    main('Hello', 'hello')
    main('HelloMyCat', 'hello')
    main('hi', 'hello')
    main('123', '123')
    main(int('123'), '123')
    main('Learn', 'Привет')
