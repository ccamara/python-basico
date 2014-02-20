for i in range(1, 5):
    print(i)
else:
    print("The for loop is over")

# Ejemplo con listas, sacado de http://www.codecademy.com/courses/python-beginner-en-pwmb1/1/6
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    number = number ** 2
    square_list.append(number)
square_list.sort()
print(square_list)