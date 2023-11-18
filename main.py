# # # a = 1
# # # b = 2
# # # c = 3
# # # # d = 10 #не обовєязково використовувати
# # # print(str(a) + str(b) + str(c))

# # # f = b + c
# # # print (str(a) + str(f))


# # # students_number1 = int(input("Введіть кількість учнів в класі 1: "))
# # # students_number2 = int(input("Введіть кількість учнів в класі 2: "))
# # # students_number3 = int(input("Введіть кількість учнів в класі 3: "))

# # # desks_number1 = students_number1 // 2 + students_number1 % 2
# # # desks_number2 = students_number2 // 2 + students_number2 % 2
# # # desks_number3 = students_number3 // 2 + students_number3 % 2

# # # print (desks_number1 + desks_number2 + desks_number3)

# # #  З початку доби пройшло n хвилин. Програма приймає це число input-ом. 
# # # Який час буде показувати електроне табло годинника ?
# # # Програма має вивести два числа - години (від 0 до 23), та 
# # # хвилини (від 0 до 59).


# # minutes_number = int(input("Введіть кількість хвилин: "))
# # hours_number = minutes_number // 60 % 24
# # minutes_number1 = minutes_number % 60
# # print(hours_number, minutes_number1, sep=':', end='!')


# # Дано текст і потрібно знайти його перше слово.

# # Даний текст містить англійські букви та пробіли.
# # На початку та у кінці пробілів немає.

# # f = input("enter text: ") + ' '
# # space = f.find(' ')
# # print(space)
# # print(f[:space])

# # Твоя задача знайти, на яку кількість нулів закінчується передане число.

# # # f = str(input("enter number"))
# # # a = str(int(f[::-1]))

# # # zero_number = len (f) - len (a)

# # # print(zero_number)

# # # Вхідний рядок складається лише з цифр. Функція повинна повернути кількість нулів від початку рядка.

# # f = input("enter number ")
# # a = str(int(f))

# # # zero_number = len (f) - len (a)

# # # print(zero_number)

# # is_active = input("Is the user active? ")
# # is_admin = input("Is the user administrator? ")
# # is_permission = input("Does the user have access? ")

# # is_active = bool(is_active)
# # is_admin = bool(is_admin)
# # is_permission = bool(is_permission)
# # access = bool(is_admin == True or (is_active == True and is_permission == True))
# # print(access)

# # work_experience = float(input("Enter your full work experience in years: "))

# # if work_experience <= 5 and work_experience > 1:
# #     developer_type = "Middle"
# # elif work_experience <= 1:
# #     developer_type = "Junior"
# # elif work_experience > 5:
# #     developer_type = "Senior"

# # print(developer_type)

# # num = int(input("Enter a number: "))

# # if num > 0:
# #     if num % 2 == 1:
# #         result = "Positive odd number"
# #     else:
# #         result = "Positive even number"
# # elif num < 0:
# #     result = "Negative number"
# # else:
# #     result = "It is zero"

# # print(result)

# # import math

# # a = int(input("Enter coefficient a: "))
# # b = int(input("Enter coefficient b: "))
# # c = int(input("Enter coefficient c: "))

# # D = b ** 2 - 4 * a * c

# # if D < 0:
# #     print ('коренів немає')
# # else:
# #     x1 = (-b + math.sqrt(D)) / (2 * a) 
# #     x2 = (-b - math.sqrt(D)) / (2 * a)

# # print(x1, x2)

# # name = "Dima"
# # for i in range(len(name)):
# # #     print(name[i])

# # # _= [print(i) for i in name]

# # name = "Dima"

# # [print(i) for i in name]


# # try:
# #     a = 3 / 0
# #     raise ValueError("aaaaayyyy")
# # except ValueError:
# #     print("This is fine")
# # except ZeroDivisionError:
# #     print("You got me")
# # else:
# #    print("Really fine")


# # num = int(input("Enter an integer number: "))

# # is_even = "Even" if num % 2 == 0 else "0 or Odd"

# # print(is_even)

# # user_name = input("enter your name: ")

# # if user_name == "Alex":
# #     print("Hello")
# # elif user_name == "Vasya":
# #     print("Hello Vasya")
# # elif user_name == "Masha":
# #     print("Hello Masha")
# # else:
# #     print("Wrong user name!")

# # # print("End")
# # age = 7
# # adult = True if age >= 18 else False
# # print(adult)

# # num = int(input("Enter the integer (0 to 100): "))
# # sum = 0
# # i = 0
# # if num <= 100 and num >= 0:
# #     while i <= num:
# #         sum = sum + i
# #         i = i + 1
# # else: 
# #     print("Введенное число не принадлежит диапозону от 0 до 100")
# # print(sum)


# # for i in range (0, 10):
# #     print(i)

# # message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# # search = "r"
# # result = 0
# # for search in message:
# #     result = len(search)

# # message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# # search = "r"
# # result = 0

# # for letter in message:
# #     if letter == search:
# #         result += 1

# # print(result)


# # while True:
# #     user_input = input("enter number: ")
# # try:
# #     x = int(user_input)
# # except ValueError:
# #     print("Should be a numer. Please try again")
# #     continue

# # break
    
    
# # first = int(input("Enter the first integer: "))
# # second = int(input("Enter the second integer: "))

# # gcd = 0
# # gcd = first if first >= second else second
# # while second % gcd != 0 or first % gcd != 0:
# #     gcd -= 1
# # print(gcd)

# # num = int(input("Enter integer (0 for output): "))
# # sum = 0
# # i = 0
# # while num != 0:
# #     for i in range(0, num+1):
# #          sum += i
# #          i += i
# #     print(sum)
# #     break
# # num = int(input("Enter integer (0 for output): "))


# # num = int(input("Enter integer (0 for output): "))
# # sum = 0
# # i = 0
# # while num != 0:
# #     for i in range(0, num+1):
# #         sum += i
# #         i += i
# #     num = int(input("Enter integer (0 for output): "))
# # print(sum)

# # num = int(input("Enter integer (0 for output): "))
# # sum = 0
# # i = 0
# # while num:
# #     if num == 0:
# #         break
# #     for i in range(0, num+1):
# #         if i % 2 == 1:
# #             continue
# #         sum += i
# #         i += i
# #     num = int(input("Enter integer (0 for output): "))
# # print(sum)

# # message = input("Enter a message: ")
# # offset = int(input("Enter the offset: "))
# # encoded_message = ""
# # for ch in message:
# #     pos = ord(ch) - ord('a')
# #     pos = (pos + offset) % 26
# #     new_char = chr(pos + ord("a"))      
# #     print(new_char)
# #     ch = ch + 1
# #     print

# # message = input("Enter a message: ")
# # offset = int(input("Enter the offset: "))
# # for ch in message:
# #     pos = (ord(ch)-ord('a'))
# #     pos = (pos + offset) % 26
# #     new_char = chr(pos + ord("a"))
# #     new_message = str(new_char)
# #     print(new_message)


# # message = input("Enter a message: ")
# # offset = int(input("Enter the offset: "))

# # encoded_message = ""

# # for ch in message:
# #     if ch.isalpha():
# #         base = ord('a') if ch.islower() else ord('A')

# #         pos = (ord(ch) - base + offset) % 26 + base

# #         ch = chr(pos)

# #     encoded_message += ch

# # print(f"ciphered text is: '{encoded_message}'")


# # pool = 1000
# # quantity = int(input("Enter the number of mailings: "))
# # try:
# #     chunk = pool / quantity
# # except ZeroDivisionError:
# #     print('Divide by zero completed!')


# # result = 0
# # operand = None
# # operator = None
# # wait_for_number = True

# # while True:
# #     while wait_for_number == True:
# #             try:
# #                 operand = input("Enter the number: ")
# #                 operand = float(operand)
# #                 if type(operand) == float:
# #                     print(result)
# #                     wait_for_number = False
# #                     break
# #                 else: continue
# #             except ValueError:
# #              print(f"\"{operand}\" is not a number. Please try again. ")
# #              continue
               
# #     while wait_for_number == False:
# #             operator = input("Enter the operation \"+\", \"-\", \"*\", \"/\" or \"=\" to get the result. ")
            
# #             if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "=":
# #                     print(f" \"{operator}\" is not \"+\", \"-\", \"*\", \"/\", \"=\". Please try again. ") 
# #             else:
# #                     if operator == "+":
# #                         result += operand 
# #                         wait_for_number = True
# #                         break
# #                     elif operator == "-":
# #                         result -= operand
# #                         wait_for_number = True
# #                         break
# #                     elif operator == "*":
# #                         result *= operand
# #                         wait_for_number = True
# #                         break
# #                     elif operator == "/":
# #                         result /= operand
# #                         wait_for_number = True
# #                     elif operand == "=" or operator == "=":
# #                         print(result)
# #                         break
                            
# # result = None
# # operator = None
# # wait_for_number = True



# # while True:
# #             if wait_for_number == True:
# #                 print(result)
# #             try:
# #                 operand = input("Enter the number: ")
# #                 operand = float(operand)
# #                 if type(operand) == float:
# #                     wait_for_number = False
# #                 else: continue
# #             except ValueError:
# #              print(f"\"{operand}\" is not a number. Please try again. ")
             
         
         
# #             if wait_for_number == False:
# #                 operator = input("Enter the operation \"+\", \"-\", \"*\", \"/\" or \"=\" to get the result. ")
            
# #             if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "=":
# #                     print(f" \"{operator}\" is not \"+\", \"-\", \"*\", \"/\", \"=\". Please try again. ") 
# #             else:
# #                     if operator == "+":
# #                         result += operand
# #                         wait_for_number = True
# #                     elif operator == "-":
# #                         result -= operand
# #                         wait_for_number = True
# #                     elif operator == "*":
# #                         result *= operand
# #                         wait_for_number = True
# #                     elif operator == "/":
# #                         result /= operand
# #                         wait_for_number = True
# #                     elif operand == "=" or operator == "=":
# #                         print(result)
                      
# # result = 0
# # operator = None
# # wait_for_number = True

# # while True:
# #     if wait_for_number == True:
# #             try:
# #                 operand = input("Enter the number: ")
# #                 operand = float(operand)
# #                 if type(operand) == float:
# #                     wait_for_number = False
# #             except ValueError:
# #              print(f"\"{operand}\" is not a number. Please try again. ")
               
# #     elif wait_for_number == False:
# #             operator = input("Enter the operation \"+\", \"-\", \"*\", \"/\" or \"=\" to get the result. ")
            
# #             if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "=":
# #                     print(f" \"{operator}\" is not \"+\", \"-\", \"*\", \"/\", \"=\". Please try again. ") 
# #             else:
# #                     if operator == "+":
# #                         result += operand 
# #                         wait_for_number = True
# #                         print(result)
# #                     elif operator == "-":
# #                         result -= operand
# #                         wait_for_number = True
# #                         print(result)
# #                     elif operator == "*":
# #                         result *= operand
# #                         wait_for_number = True
# #                         print(result)
# #                     elif operator == "/":
# #                         result /= operand
# #                         wait_for_number = True
# #                         print(result)
# #                     elif operand == "=" or operator == "=":
# #                         print(f"result: {result}") 
# #                         break               

# # result = None
# # operand = None
# # operator = None
# # wait_for_number = True

# # while True:
# #     if wait_for_number:
# #         try:
# #             operand = float(input("Enter the number: "))
# #             wait_for_number = False
# #         except ValueError:
# #             print(f"\"{operand}\" is not a number. Please try again.")
# #             continue

# #     operator = input("Enter the operation \"+\", \"-\", \"*\", \"/\" or \"=\" to get the result: ")

# #     if operator == "=":
# #         print(f"result: {result}")
# #         break

# #     if operator not in ("+", "-", "*", "/"):
# #         print(f"\"{operator}\" is not a valid operator. Please try again.")
# #         continue

# #     while True:
# #         try:
# #             operand2 = float(input("Enter the next number: "))
# #             if operator == "+":
# #                 result = operand + operand2
# #             elif operator == "-":
# #                 result = operand - operand2
# #             elif operator == "*":
# #                 result = operand * operand2
# #             elif operator == "/":
# #                 if operand2 == 0:
# #                     print("Division by zero is not allowed.")
# #                 else:
# #                     result = operand / operand2
# #             operand = result
            
# #             break
# #         except ValueError:
# #             print(f"\"{operand2}\" is not a number. Please try again.")
            
# # username = None

# # def invite_to_event(username):
# #     print(f"Dear {username}, we have the honour to invite you to our event")

# # username = input("Enter your name: ")

# # invite_to_event(username)

# # initial_pin = '0123'
# # n= 0
# # max_tries = 3


# # while n < max_tries:
    
# #     user_pin = input('Enter your pin: ')

# #     if len(user_pin) >= 4:
# #         if initial_pin == user_pin:
            
# #             amount = int(input("How much?: "))
            
# #             if amount > 0:
            
# #                 print(f"Take your amount!")
# #                 break
# #         else:
# #             print('Sorry, wrong pin. Try again please!')
# #             print(f'You have {max_tries - n - 1} tries')
# #     else:
# #         print('Pin should be 4 or 6')
    
# # print('Good Bye!')


# # from random import randint


# # SIZE_N = 5
# # SIZE_M = 5

# # char_x = 3
# # char_y = 2

# # exit_x = randint(0, SIZE_N-1)
# # exit_y = randint(0, SIZE_M-1)

# # while True:
    
# #     world_map = ''

# #     for j in range(SIZE_M):

# #         row = ' |'

# #         for i in range(SIZE_N):
            
# #             if char_x == i and char_y == j:
# #                 if char_x == exit_x and char_y == exit_y:
# #                     row += 'W|'
# #                 else:
# #                     row += 'X|'
# #             elif exit_x == i and exit_y == j:
# #                 row += 'O|'
# #             else:
# #                 row += ' |'
            
# #         world_map += f'{row}\n'

    
# #     print(world_map)
    
# #     if char_x == exit_x and char_y == exit_y:
# #         print("You won!!!")
# #         break
    
# #     direction = input('Enter direction (w / a / s / z):  ')
    
# #     if direction == 'w' and char_y > 0:
# #         char_y -= 1
    
# #     elif direction == 'z' and char_y < SIZE_N-1:
# #         char_y += 1
        
# #     elif direction == 's' and char_x < SIZE_M-1:
# #         char_x += 1
    
# #     elif direction == 'a' and char_x > 0:
# #         char_x -= 1


# # def print_hello():
# #     print('Hello')
    
    
# # def print_bye():
# #     print('Bye')
    
# # print_hello()
# # print_bye()

# # Задача 1
# # Є три числа. 
# # Визначте скільки чисел співпадає. Треби вивести 0, 2 чи 3.
# # 10 5 10 -> 2
# # 17 17 -9 -> 2
# # 5 2 4 -> 0
# # 1 1 1  -> 3

# # a, b, c = 1, 2, 3

# # if b == a == c:
# #     print(3)

# # elif a == b or a == c or b == c:
# #     print(2)
    
# # else:
# #     print(0)

# # def ss(a, e, s):
# #     if s > a*e:
# #         return False
# #     if s % a == 0 or s % e == 0:
# #         return True
# #     else: 
# #         return False
    
# # Задача 2
# # Качка плаває в прямокутному пруду розміром n на m метрів.
# # Це розумна, бойова українська качка.
# # Вона знає, що під час тревоги треба якнайшвидше дістатись берега
# # і сховатись у кущах. 
# # Коли залунала сирена вона одразу визначила, 
# # що до найдовшої сторони пруда їй плисти x метрів,  
# # а до короткої сторони пруда - y  метрів.
# # Визначте її найкоротший шлях до берега.
# # 23 52 8 43 -> 8

# # 18 90 3 63 -> 3
# # 73 63 56 8 -> 7

# # 4. Дано два числа A B.
# #    Вивести всі числа між А та B у спадному поряду

# # a = int(input("enter num1"))
# # b = int(input("enter num2"))

# # a, b = 60, 40
# # step = 1 
# # if a > b:
# #     step = -step
# # for i in range(b-1, a, step):
# #     print(i, end = " ")
    
# #   *
# #   ***
# #   *****
# #   *******
# #   *********
  
# # for i in range(1, 10, 2):
# #     print("*" * i)

# #         *
# #       ***
# #     *****
# #   *******
# # *********

# # for i in range(1, 10, 2):
# #     b =('*' * i)
# #     print(b.center(9))
    
# #   Задача 8.
# # Курець бросає палити. 
# # Він обіцяє собі кожень день палити на 10 % менше 
# # ніж в попередній день, округляючи до меншого.
# # Зазвичай він випалює в день 30 цигарок.
# # Через скільки днів він бросить палити?


# # num_days = 0

# # num_cig = 30

# # while num_cig > 0:
# #     num_cig = int(num_cig - num_cig / 10)
# #     num_days += 1
    
# # print(num_days)

# # def calculate_sum(x, y):
# #     return x - y

# # result = calculate_sum(y=5, x=7)
# # print(result)

# # result = calculate_sum(7, 16)
# # print(result)

# # result = calculate_sum(15, 1)
# # print(result)

# # base_rate = 40
# # price_per_km = 10
# # total_trip = 0




# # def calculate_trip_price(distance_km):
# #         global total_trip
        
# #         trip_price = base_rate + distance_km * price_per_km
        
# #         total_trip += 1

# #         return trip_price

# # print(calculate_trip_price(20))
# # print(total_trip)

# # price = 0
# # discount = 0


# # def discount_price(price, discount):
    
# #     def apply_discount():
        
# #         nonlocal price
        
# #         price = price - price * discount     

# #     return discount_price

# # x = discount_price(20, 0.2)

# # print(x)

# # first_name = ""
# # last_name = ""
# # middle_name = ""

# # def get_fullname(first_name, last_name, middle_name=None):
# #     if not middle_name:
# #         return f"{first_name} {last_name}"
# #     else:
# #         return f"{first_name} {middle_name} {last_name}"

# # get_fullname("Олександр", "Баран")

# # result = get_fullname("Олександр", "Баран")
# # print(result)

# # def format_string(string, length):
# #     space_num = (length - len(string)) // 2
# #     if len(string) >= length:
# #         return string
# #     else:
# #         return " " * space_num + string
  
# # result = format_string("srkjhfkkjrhjkgkdkj", 49)   
# # print(result)

# # def first(size, *args):
# #     sum = 0
# #     sum = size + len(args)

# #     return sum

# # result = first(5, 'first', 'second', 'third')
# # print(result)

# # def cost_delivery(*quantity, discount=0):
    
# #     price_first = 5
# #     price_other = 2
# #     if quantity[0] == 1:
# #         cost_delivery = price_first * (1 - discount)
# #     elif quantity[0] > 1:
# #         cost_delivery = price_first * (1 - discount)  + (quantity[0] - 1) * price_other * (1 - discount) 
# #     else:
# #         cost_delivery = 0
           
# #     return cost_delivery

# # result = cost_delivery(3, 3)
# # print(result)


# # def fibonacci(n):
# #     if n <= 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibonacci(n - 1) + fibonacci(n - 2)
        

# # result = fibonacci(15)
# # print(result)


# # data = [8, 1, 0, 15, 45]
# # def prepare_data(data):
# #     data.sort()
# #     data.pop(0)
# #     data.pop(-1)

# #     return data

# # result = prepare_data(data)
# # print(result)

# # items = []
    
# # def format_ingredients(items):
# #     if len(items) <= 1:
# #         string = ", ".join(items)
# #         return string
# #     else:
# #         final_item = items[-1]
# #         items.pop(-1)
# #         string = ", ".join(items)
# #         return f"{string} and {final_item}"
    

# # grade = {"F":1, "FX":2, "E":3, "D":3, "C":4, "B":5, "A":5}
# # def get_grade(key):
# #     return grade.get(key)
    
# # grade_description = {"F":"Unsatisfactorily", "FX":"Unsatisfactorily", "E":"Enough", "D":"Satisfactorily", "C":"Good", "B":"Very good", "A":"Perfectly"}

# # def get_description(key):
# #     return grade_description.get(key)

# # result_1 = get_grade('FX')    
# # result_2 = get_description('FX')

# # print(result_1)
# # print(result_2)

# # taget_value = 0
# # data = {"F":1, "FX":2, "E":3, "D":3, "C":4, "B":5, "A":5}
# # def lookup_key(data, target_value):
# #     keys = []
# #     for key, value in data.items():
# #         if value == target_value:
# #             keys.append(key)
# #     return keys
    
# # result = lookup_key(data, 3)
# # print(result)


# # def main():
# #     table = [
# #         [1, 2, 3],
# #         [4, 5, 6],
# #         [7, 138, 9]
# #     ]
    
# #     for y in range(len(table)):
# #         for x in range(len(table[y])):
# #             print(f" | {table[y][x]:_^5}|", end="")
# #         print()

# # if __name__ == "__main__":
# #     main()

# # # put your python code here
# # a = int(input())
# # b = a + 1
# # c = a + 2
# # print(a, b, c, sep = "\n")

         

# # # put your python code here
# # a = int(input())
# # volume = a ** 3
# # squere = 6 * a ** 2
# # print('Объем', '=', volume)
# # print('Площадь полной поверхности', '=', squere)

# # a, b, c, d = int(input()), int(input()), int(input()), int(input())
# # print(a + b + c + d)

# # a = 82 // 3 ** 2 % 7
# # print(a)

# # a = 7

# # if a >= 2 and a <= 17:
# #     b = 3
# #     p = a * a + b * b
# # else:
# #     b = 5

# # p = (a + b) * (a + b)
# # print(p)

# # b = 5
# # print(type(b))
    
# # put your python code here
# # num = int(input())

# # if num not in range (0,36):
# #     print('ошибка ввода')  
# # elif num == 0:
# #     print('зеленый')
# # elif (num % 2 == 0 and num in range (1, 11)) or (num % 2 == 1 and num in range (11, 19)) or (num % 2 == 0 and num in range (19, 30)) or  (num % num % 2 == 1 and num in range (29, 37)):
# #     print('черный')
# # else:
# #     print('красный')
    
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a2 > b1 or a1 > b2:
#     print('пустое множество')
# elif a2 == b1:
#     print(a2)
# elif b2 == a1:
#     print(a1)
# elif a2 > a1 and b2 > b1:
#     print(a2, b1)
# elif a1 > a2 and b1 > b2:
#     print(a1, b2)
# elif a1 > a2 and b2 > b1:
#     print(a1, b1)
# elif a2 > a1 and b1 > b2:
#     print(a2, b2)
# elif a1 == a2  and b1 == b2:
#     print(a1, b1)
# elif a2 < a1 and b1 == b2:
#     print(a1, b1)
# elif a2 < a1 and b1 == b2:
#     print(a1, b1)
# elif a1 == a2 and b1 < b2:
#     print(a1, b1)
# elif b1 > b2 and a1 == a2:
#     print(a2, b2)
# elif a2 > a1 and b1 == b2:
#     print(a2, b2)

    
# command: add/remove
# item: contains letters only
# amount: contains digits only
#
# $command $item $amount 
# def parse_input(sequence):
#     tokens = sequence.split(" ") # ['$command", "$item", "$amount"]
#     if len(tokens) != 3:
#         return None

# def main():
#     while True:
#         sequence = input(">>> ")
        
#         if sequence == "exit":
            
        
#         parsing_result = parse_input(sequence)
#         if parsing_result is None:
#             print("Wrong command format")
#             continue

# if __name__ == "__main__":
#     main()


# put your python code here








# 2. Дан текстовий рядок. В ньому можуть бути подвійні пробіли.
# Видаліть всі зайві пробіли.

# string1 = 'jerhgkjkjethr tegjhgjthkjrh  jkherrhfjkhekrhkj rejfh  jh!'
# string2 = string1.replace("  ", " ")

# print(string2)

# 3.Дан рядок.
# НАйдіть в ньому другу букву "а". Виведіть індекс.
# Якщо є тільки одна  - виведить "alone", якщо взагалі нема
# виведіть None

# a = 'adkrnfrrngl krjlka tkgtl jkhkkjhkhaj'

# w = a.find('a')

# if w == -1:
#     print('None')
# else:
#     a1 = a[w+1:]
#     w1 = a1.find('a')
#     if w1 == -1:
#         print('alone')
#     else: 
#         print(w1)
    
# b = [2, 4, 6, 8, 1, 3, 5, 1, 1]
# a = set(b)
# len(a)
# print(len(a))


# a = [1, -1, 2, -2, 5, 6]
# b = [-1, -2, 5, 2]

# print(sorted(a, key=abs))

# Наприклад 1 2 3 2 3 4
# Для кожного числа виведітть  yes  чи no, якщо це число раніше 
# зустрічалось в цієї послідовності.
# numbers = [int(s) for s in input().split()]

# Наприклад 1 2 3 2 3 4
# Для кожного числа виведітть  yes  чи no, якщо це число раніше 
# зустрічалось в цієї послідовності.
# numbers = [int(s) for s in input().split()]

# string1 = '1, 2, 3, 2, 3, 4'
# list1 = string1.split(", ")

# for i, el in enumerate(list1):
#     if el in list1[0: i]:
#         print('YES')
#     else:
#         print('NO')
        
#  5. Є великий текст.
# Визначте кількість унікальних слів.
# Пунктуацію треба прибрати. 
# Слова з великої літери і маленької вважати однаковими.

# text = '''
# The other two, slight air, and purging fire,
# Are both with thee, wherever I abide,
# The first my thought, the other my desire,
# These present-absent with swift motion slide.
# For when these quicker elements are gone
# In tender embassy of love to thee,
# My life being made of four, with two alone,
# Sinks down to death, oppressed with melancholy.
# Until life's composition be recured,
# By those swift messengers returned from thee,
# Who even but now come back again assured,
# Of thy fair health, recounting it to me.
# This told, I joy, but then no longer glad,
# I send them back again and straight grow sad.
# '''

# text1 = (text.lower().replace(',', ' ').replace('.', " ").replace('-', " "))
# list1 = text1.split()


# a = dict.fromkeys(list1, 0)

# for word in list1:
#     a[word] += 1
    
# b = dict()
# for k, v in a.items():
#     b[v] = b.get(v, []) + [k]
# print(b)    

