#Задание2
#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением "27.05.2019"
#Выведите на экран длину словаря

#Список
key = {
    "country": "Россия"
}
#Проверьте, есть ли в словаре ключ country
print(key.get("country"))

#Выведите значение по-умолчанию "Россия" для ключа country
print(key.get("country", "0"))

#Добавьте в словарь элемент date со значением "27.05.2019"
key["date"] = "27.05.2019"

#Выведите на экран длину словаря
print(key)