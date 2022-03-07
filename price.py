#Задание 1
#ФУНКЦИИ

#Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два 
#параметра, приводит их к строке и отдает объединенными через разделитель delimiter
#Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в 
#переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    two = str(two).upper()
    summ = str(one) + str(delimiter) + str(two)
    #return str(one) + str(delimiter) + two
    return summ.upper()
    
a = 'Learn'
b = 'python'
#summ = str(one) + str(delimiter) + str(two)
summ_print = get_summ(one=a, two=b, delimiter='!')

print('Задание 1: ' + summ_print)

#Задание 2
#Создайте в редакторе файл price.py
#Создайте функцию format_price, которая принимает один аргумент price
#Приведите price к целому числу (тип int)
#Верните строку "Цена: ЧИСЛО руб."
#Вызовите функцию, передав на вход 56.24 и положите результат в переменную
#Выведите значение переменной с результатом на экран

def format_price(_jopa):
    print('Цена: {} руб.'.format(_jopa.round()))

print_price = input('Задание 2: Введите число 56.24: ')
print(format_price(print_price))