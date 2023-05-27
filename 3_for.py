"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def count_sold_avg(items_sold):
        sold_sum = 0
        for sold in items_sold:
            sold_sum += sold
        return sold_sum

    item_avg_sum = 0
    for one_product in products:
        item_avg = count_sold_avg(one_product['items_sold'])
        test = round(item_avg / len(one_product['items_sold']), 1)
        print(f'Задание 1. Суммарное колличество продаж всех товаров марки {one_product["product"]}: {item_avg}')
        print(f'Задание 2. Среднее колличество продаж товара марки {one_product["product"]}: {test}')
        item_avg_sum += item_avg

    print(f'Задание 3. Суммарное колличество продаж всех товаров: {item_avg * len(products)}')

    products_avg = item_avg_sum / len(products)
    print(f'Задание 4. Среднее колличество продаж всех товаров: {products_avg}')

if __name__ == "__main__":
    main()
