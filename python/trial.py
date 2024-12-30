word = "hello world"
remove_space = " ".join(word.split()).lower()
length = len(remove_space)

print(remove_space)


def division(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        return "please enter the denominator"


print(division(denominator=10, numerator=100))



def calcul(first_number=2, second_number=100, opperator="+"):
    if opperator == "+":
        return first_number + second_number
    else:
        if second_number != 0:
            return first_number / second_number
        else:
            return "Please enter a denominator"


calcul(opperator="-")
