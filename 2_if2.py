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


from pickletools import string1



def main(str1, str2):

  """
  Эта функция вызывается автоматически при запуске скрипта в консоли
  В ней надо заменить pass на ваш код
    """
  a = not(type(str1) is str)
  b = not(type (str2) is str)
  c = a or b
  #print(a)
  #print(b)
  #print(c)
  if c:
    comparison = 0
  elif len(str1) == len(str2):
    comparison = 1
  elif str2 == 'learn':
    comparison = 3
  elif len(str1) > len(str2):
    comparison = 2
  return(comparison)
  
str1=''
str2=''
print(main('Строка', 45))
print(main(23, 'Строка'))
print(main(324, 523))
print(main('Строка1', 'Строка2'))
print(main('Строка1 длинее', 'Строка 2'))
print(main('Строка1', 'learn'))


if __name__ == "__main__":
    main(str1, str2)