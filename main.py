# # a = 1
# # b = 2
# # c = 3
# # # d = 10 #не обовєязково використовувати
# # print(str(a) + str(b) + str(c))

# # f = b + c
# # print (str(a) + str(f))


# # students_number1 = int(input("Введіть кількість учнів в класі 1: "))
# # students_number2 = int(input("Введіть кількість учнів в класі 2: "))
# # students_number3 = int(input("Введіть кількість учнів в класі 3: "))

# # desks_number1 = students_number1 // 2 + students_number1 % 2
# # desks_number2 = students_number2 // 2 + students_number2 % 2
# # desks_number3 = students_number3 // 2 + students_number3 % 2

# # print (desks_number1 + desks_number2 + desks_number3)

# #  З початку доби пройшло n хвилин. Програма приймає це число input-ом. 
# # Який час буде показувати електроне табло годинника ?
# # Програма має вивести два числа - години (від 0 до 23), та 
# # хвилини (від 0 до 59).


# minutes_number = int(input("Введіть кількість хвилин: "))
# hours_number = minutes_number // 60 % 24
# minutes_number1 = minutes_number % 60
# print(hours_number, minutes_number1, sep=':', end='!')


# Дано текст і потрібно знайти його перше слово.

# Даний текст містить англійські букви та пробіли.
# На початку та у кінці пробілів немає.

# f = input("enter text: ") + ' '
# space = f.find(' ')
# print(space)
# print(f[:space])

# Твоя задача знайти, на яку кількість нулів закінчується передане число.

# # f = str(input("enter number"))
# # a = str(int(f[::-1]))

# # zero_number = len (f) - len (a)

# # print(zero_number)

# # Вхідний рядок складається лише з цифр. Функція повинна повернути кількість нулів від початку рядка.

# f = input("enter number ")
# a = str(int(f))

# zero_number = len (f) - len (a)

# print(zero_number)

# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")

# is_active = bool(is_active)
# is_admin = bool(is_admin)
# is_permission = bool(is_permission)
# access = bool(is_admin == True or (is_active == True and is_permission == True))
# print(access)

# work_experience = float(input("Enter your full work experience in years: "))

# if work_experience <= 5 and work_experience > 1:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# elif work_experience > 5:
#     developer_type = "Senior"

# print(developer_type)

# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print ('коренів немає')
else:
    x1 = (-b + math.sqrt(D)) / (2 * a) 
    x2 = (-b - math.sqrt(D)) / (2 * a)

print(x1, x2)