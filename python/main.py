# # Question One
# num_one = 10
# num_two = 5


# # Add
# print(f"Add : {num_one + num_two}")
# # Subtract
# print(f"minus: {num_one - num_two}")
# # Multiply
# print(f"mul : {num_one * num_two}")
# # divide
# print(f"divide : {num_one / num_two}")
# # Interger divide  will always round down
# print(f"divide interger : {num_one // num_two}")
# # a remainder of a number(modulo)
# print(f"remainder(modulo) : {num_one % num_two}")
# # exponential like saying x raised to the power y ,  y is the exponent
# print(f"Exponential : {num_one ** num_two}")

# # assignment operators

# num_one += num_two
# print(f"num_one = num_one + num_two : {num_one}")
# num_one -= num_two
# print(f"num_one -= num_one - num_two : {num_one}")
# num_one *= num_two
# print(f"num_one *= num_one * num_two : {num_one}")
# num_one /= num_two
# print(f"num_one /= num_one / num_two : {num_one}")
# num_one //= num_two
# print(f"num_one //= num_one // num_two : {num_one}")
# num_one %= num_two
# print(f"num_one %= num_one % num_two : {num_one}")
# num_one **= num_two
# print(f"num_one **= num_one ** num_two : {num_one}")


# # logical operators
# active = True
# offline = False

# print("Are bot True ?", active & offline)
# print("At least One is true", active or offline)
# print("opposite of original boolean", not active)

# # identity operators
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
# # it will check the identity in memory and not tha value of this variable

# # will return false because when creating a list or others will have a new identity in memory
# print(f" a is b : {a is b}")
# print(f" a is b : {a == b}")
# # true
# print(f" a is not b : {a is not b}")
# # true because c is  refrenced to a so same identity
# print(f" a is c : {a is c}")

# # membership operators

# list_of_nums = [1, 2, 3, 4, 5]
# name = "Nur"
# # like basic english which is easy to understand
# # true
# print(f"5 in list_of_nums : {5 in list_of_nums}")
# # false
# print(f"6 in list_of_nums : {6 in list_of_nums}")
# # true
# print(f"6 in list_of_nums : {6 not in list_of_nums}")
# # false - case sensitive
# print(f"check if n in Nur : {"n" in name}")
# # true
# print(f"check if n in Nur : {"n" in name.lower()}")
# print(f"check if N in Nur : {"N" in name}")


# # Question 2
# input_one = int(input("Enter first number: "))
# input_two = int(input("Enter second number: "))
# method = input("Which method : ")

# if method == "+":
#     result = input_one + input_two
# elif method == "-":
#     result = input_one - input_two
# elif method == "*":
#     result = input_one * input_two
# elif method == "/":
#     result = input_one / input_two
# elif method == "//":
#     result = input_one // input_two
# elif method == "**":
#     result = input_one**input_two
# elif method == "%":
#     result = input_one % input_two
# else:
#     result = "Invalid method"


# print(f"The result is: {result}")

# # Question 3
# num_1 = 2
# num_2 = 4
# # false
# print(num_1 == num_2)
# # true
# print(num_1 != num_2)
# # false
# print(num_1 > num_2)
# print(num_1 >= num_2)
# # true
# print(num_1 < num_2)
# print(num_1 <= num_2)


# # Question 4

# a_one = int(input("Enter first num :"))
# a_two = int(input("Enter second num :"))


# def calculate_average(a, b):
#     return a / b


# print(calculate_average(a_one, a_two))

# # Question 5
# num = int(input("Enter a num: "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


# # Question 6

# sting_one = "hello"
# string_two = "world"

# print(string_two + " " + string_two)

# # Question 7
# numbers = [1, 5, 7, 4, 3, 2]
# print(numbers.sort())


# def is_palindrome():
#     text = input("Enter a word or phrase: ")    
#     cleaned_text = text.replace(" ", "").lower()
    
#     # Reverse the cleaned text using slicing
#     reversed_text = cleaned_text[::-1]
    
#     if cleaned_text == reversed_text:
#         print(f"'{text}' is a palindrome!")
#     else:
#         print(f"'{text}' is not a palindrome.")

# # Run the palindrome check
# is_palindrome()

import packages.users.user