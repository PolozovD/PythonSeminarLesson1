# print(100 * 5)

# print("Your auto geted", 100 * 5, "km")

# speed = 100
# time = 6
# distance = speed * time
# print("Your auto geted", distance, "km")


# speed = input("Input speed ")
# time = input("Input time ")
# distance = speed * time
# print("Your auto get", distance, "km")




# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# import math
# n = int(input("Input days of marshrut: "))
# m = int(input("Input all maarschrut: "))
# days = m / n
# print(f"Days need ", {math.ceil(days)})


# import math

# distance_per_day = int(input("Введите число n, сколько за день проезжает автомобиль "))
# distance = int(input("Введите число m, расстояние, которое нужно проехать "))
# print("Для преодоления расстояния m необходимо ", int((distance / distance_per_day)))
# print(math.ceil(distance / distance_per_day))
# print((distance + distance_per_day + 1) // distance_per_day)


# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.


# class_1 = int(input("Введите количество учеников 1ого класса "))
# class_2 = int(input("Введите количество учеников 2ого класса "))
# class_3 = int(input("Введите количество учеников 3его класса "))
# print(
#     class_1 // 2 + class_1 % 2 + class_2 // 2 + class_2 % 2 + class_3 // 2 + class_3 % 2
# )


# import math
# n1 = int(input("Input count 1 class: "))
# n2 = int(input("Input count 2 class: "))
# n3 = int(input("Input count 3 class: "))

# partsClass1 = math.ceil(n1 / 2)
# partsClass2 = math.ceil(n2 / 2)
# partsClass3 = math.ceil(n3 / 2)

# partSum = partsClass1 + partsClass2 + partsClass3

# print(f"Parts is need: {partSum}")



# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# i = int(input("Введите номер вагона с головы состава: "))
# j = int(input("Введите фактический номер вагона: "))
# if (i == j):
# print("Недостаточно данных для решения")
# else:
# print(j + i - 1)


# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# year = int(input("Input year: "))
# if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
#     print(f"Yes")
# else:
#     print(f"No")


# Кредит. Клиент вводит свои данные и какой он хочет кредит. 
# Если сумма ежемесячных платежей больше половины ЗП или дата окончания уплаты кредита выходит за 50 лет - кредит не дадут

# salary = int(input("Input your salary: "))
# age = int(input("Input your age:"))
# credit = int(input("Input the amount you want to borrow: "))
# month = int(input("Input for how many months: "))

# if credit / month > salary / 2 or age / 12 + month > 50 * 12:
#     print(f"The loan is not approved for you")
# else:
#     print(f"Congratulations, the loan is approved")





# Ввести два числа и определить какое больше

# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))

# if num1 > num2:
#     print("First number is great")
# elif num1 < num2:
#     print("Second number is great")
# else:
#     print("The first number is equal to the second4")


h = 6
print(['yes', 'no'][h%3!=0])




