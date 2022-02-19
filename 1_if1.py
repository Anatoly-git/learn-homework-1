"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = input('Укажите свой возраст: ')
  
def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
      age = int(age)
    except ValueError:
      age = 0
    if age <= 0:
      status = 'Возраст указан не верно'
    elif 0 < age < 7:
      status = 'Вы учитесь в детском саду'
    elif 7 <= age < 18:
      status = 'Вы учитесь в школе'
    elif 18 <= age < 23:
      status = 'Вы учитесь в ВУЗе'
    else:
      status = 'Вы ходите на работу'
    return(status)
    
print(main(age))
if __name__ == "__main__":
    main(age)
