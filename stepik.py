# z = 0
# for i in range(0, 10 ** 11):
#     if i % 23347759 == 0:
#         z += 1
#         print(f"{i}     {z}")

# n = 0
# number = 23347759
# while number <= 10 ** 20:
#     number +=  number 
#     n += 1
#     print(f'{number}     {n}')
    
# m, n = int(input()), int(input())
# for i in range(m, n-1, -1):
#         if i % 2 == 1:
#             print(i) 
    
# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')





# fh = open('test99999999999.txt', 'r')
# all_file = fh.read()
# b = len(all_file)  
# num = None

# counter = 0
# for num in range(0, b-1):
#     if num == "12":
#         counter += 1
# print(counter)



# print(b)


# fh.close()

# s = 2 ** 420
# b = '\nI do not understand\n'


# fh = open('test123.txt', 'a')
# symbols_written = fh.write(b)
# print(symbols_written)  # 6
# fh.close()

# fh = open('test123.txt', 'r')
# buffer = fh.read(5)
# print(buffer)

# buffer = fh.read(5)
# print(buffer)

# fh.tell()

# fh.close()


# import random

# text = "hello world"

# print(f"Clean text: {text}")
# key = [random. randint (0, 255) for _ in range(len(text))]
# print (f"Key: {key}")
# # cypher_char = text[0] ^ key[0]
# byte_text = text.encode()
# cypher_char = byte_text[0] ^ key[0]
# print(f"Cypher_char: {cypher_char}")
# cypher_char ^= key[0]
# print(f"Decrypted cypher char: {bytes([cypher_char]).decode()}")

# c = 'rekgjlkrtwhjlkjrlkjhlk'
# print(b'{c}')

# total = 0
# for i in range(1, 6):
#     total += i
#     print(i, total)
    
# print(total)

# put your python code here

# a, b = int(input()), int(input())

# for i in range(a, b+1):
#     if ((i ** 3) % 10 == 4) or ((i ** 3) % 10 == 9):
#         print(i)

# put your python code here



# text = input()
# char = input()
# counter = 0

# for character in text:
#     if character == char:
#         counter += 1
# print(f'Character {char} occurres {counter} times')
    
# # Получаем ввод у пользователя
# s = input()

# # Обявляем словарь (store) (ключи будут символами, а значения будут кол-вом появлений)
# store = {}

# # Проходимся по каждому символу в строке
# for char in s:
#     char = char.strip() # Очищаем строку от пробелов с помощью strip

# # Если строка это пробел то пропускаем
#     if not char:
#         continue
    
# # Если символ уже находится в словаре, то увеличиваем кол-во появлений
#     if char in store.keys():
#         store[char] += 1
        
# # Если нет, то ставим 1
#     else:
#         store[char] = 1

# # Проходимся по ключам & значениям словаря
# for char, n in store.items():
#     print(f"Character {char} occurs {n} times")  # Виводим символ и кол-во появлений

# n = int(input())
# for i in range(n-1):
#     x = int(input())
#     x += x
#     print(f'{i}   {x}')
# print(n)


# n = int(input())
# a = []
# for _ in range(n):
#     x = int(input())
#     a.append(x) 
        
# a.sort()
# print(a)
# print(a[-1])
# print(a[-2])

# n = int(input())
# flag = True

# for _ in range(n):
#     x = int(input())
#     if x % 2 == 1:
#         flag = False
    
# if flag == False:
#     print('NO')
# else:
#     print('YES')

# put your python code here



# n = int(input())

# x_current, x_next = 1, 1

# print(x_current, end=" ")

# for _ in range(n - 1):
#         print(x_next, end=" ")
#         x_current, x_next = x_next, x_current + x_next
   

# while True:
#     word = input()
#     if word == 'КОНЕЦ' or word == 'конец':
#         break
#     print(word)

# num = int(input())

# while num % 7 == 0:
#     print(num)
#     num = int(input())

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
#    print(mult)
# print(mult)

n = int(input())
i = 2

while i < n:
    n = n % i
    if n % i == 0:
        print(i)
        break 
    i += 1
   
     









