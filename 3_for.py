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

from pprint import pprint


sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sales (product_score):
    scores_sum = 0
    for score in product_score:
        scores_sum += score
    return scores_sum

def mod_sale(sale):
    mod_sales = sales
    total_sale = 0
    for one_product in mod_sales:
        product_sum = count_sales(one_product['items_sold'])
        product_sum_avg = product_sum / len(one_product['items_sold'])
        #print(f'Суммарено количество продаж {one_product["product"]}: {product_sum}')
        #print(f'Среднее количество продаж {one_product["product"]}: {product_sum_avg}')
        total_sale += product_sum
        one_product['sum_sold'] = product_sum
        one_product['sum_avg_sold'] = product_sum_avg
    for one_product in mod_sales:
        print(f'Суммарное количество продаж {one_product["product"]}: {one_product["sum_sold"]}')
    for one_product in mod_sales:    
        print (f'Среднее количество продаж {one_product["product"]}: {one_product["sum_avg_sold"]}')
    for one_product in mod_sales:    
        print (f'Процент продаж {one_product["product"]}: {int(one_product["sum_sold"] / total_sale * 100)}%')

    total_sales_avg=round(total_sale / len(sales), 1)
    mod_sales.append({'total_sum_sold':total_sale, 'total_sum_avg_sold':total_sales_avg}) 
    #pprint(mod_sales)
    
    
    
    print(f'Общее количество продаж: {total_sale}')
    print (f'Среднее количество продаж по всем продуктам: {total_sales_avg}')
  
    #pprint(mod_sales)    
    return mod_sales



if __name__ == "__main__":
    mod_sale(sales)
