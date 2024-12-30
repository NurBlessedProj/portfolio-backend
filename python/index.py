# # name = "p"
# # first_name = "jeans"

# # print(f"hello my name is  {first_name} {name} and i am {age}")

# # age = 30
# # if(age % 10 == 0): print(f"{age} is divissable  ")
# # else : print("not divissable")

# days= {"mon":1, "month":12, "year":24}
# numbers = {1,2,3,4,2}
# for number in numbers:
#   print(number)
# # array = ["day", "month", "year"]
# # print(array[2])

#   age=40
#   if age >10:
#     print(f"{age}")

# a = 10  # True (1 in binary)
# b = 5 # False (0 in binary)

# print(f"original :{b}")
# print(f"not used :{~ b}")

# if a & (not b):
#     print("Both are true")
# else:
#     print("At least one is false")

# def greet():
#   if a%b == 2:
#     return True
#   else : return False

# print(greet()
# import ma


# complex_num = 2 + 3j

# # Accessing real and imaginary parts
# real_part = complex_num.real
# imaginary_part = complex_num.imag

# print(f"Real part: {real_part}")
# print(f"Imaginary part: {imaginary_part}")

# complex_num1 = 2 + 3j
# complex_num2 = 1 + 4j

# # Adding two complex numbers
# sum_result = complex_num1 + complex_num2
# print(f"Sum: {sum_result}")

# my_list = (1, 2, 3,5,3, "hello")
# print(my_list)

# list_one = [1,2,3,4]
# diction = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# print(diction.values())
# list_two= [5,6,7,8]
# list_one.extend(list_two)

# print(list_one)

# a, b,c = 15, 7, 5
# print(c)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum:", a + b)


# a, b = 20, 30
# print("Average:", (a + b) // 2)

# num = 10
# print(f"Even {num}" if num % 2 == 0 else "Odd")

# str1, str2 = "Hello", "World"
# print(str1 + " " + str2)

# nums = [4, 2, 8, 1]
# nums.sort()
# print(nums)

# print("abc" >= "s")  # Lexical comparison

# numbers = [1,2,3,4,5]

# for num in numbers:
#     print(num)

# print("a"  "A")  # Lexical comparison

# name = "Charlie"
# if name < "Delta":
#     print(f"{name} comes before Delta in dictionary order.")

# age = int(input("Enter your age :"))

# if age < 12:
#     reduction = 50
#     print(f"You get a {reduction} % discount")
# elif age <= 19:
#     reduction = 25
#     print(f"You get a {reduction} % discount")
# elif age >= 65:
#     reduction = 30
#     print(f"You get a {reduction} % discount")
# else:
#     print("You pay full price")


# # Match (switch case)
# match age:
#     case _ if age < 12:
#         reduction = 50
#         print(f"You get a {reduction} % discount")
#     case _ if age <= 19:
#         reduction = 25
#         print(f"You get a {reduction} % discount")
#     case _ if age >= 65:
#         reduction = 30
#         print(f"You get a {reduction} % discount")
#     case _:
#         print("You pay full price")


# lists = ["orange", "apple", "ananas"]

# for index, list in enumerate(lists):
#     print(list)
#     print(index)

n = int(input("Enter a number :"))

# sum = 0
# for n in range(1, n + 1):
#     sum += n
# print(n)
# print("Sum of numbers is", sum)

# OR

if n <= 0:
    print("Please enter a positive number")
else:
    result = sum(range(1, n))
    print(f"Result equal to {result}")




