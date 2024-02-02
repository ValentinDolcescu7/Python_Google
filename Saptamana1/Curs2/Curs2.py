"""
This is my first program
"""
from copy import deepcopy

# This is an inline comment
print('Hello, World!')

a = 5
b = 7
c = a * b
print('c =', c)
numbers = [1, 2, 3, 4, 5, 6]
name = 'Valentin'

if 1 in numbers:
    print('1 e gasit')

if 'x' not in name:
    print('x nu e gasit')
else:
    print('x e gasit')

my_var = 3

my_var += 1  # my_var = my_var +1
my_var -= 1  # my_var = my_var -1
print('My_var are valoarea:', my_var)


empty_str = ""
print("Empty string contine: ", empty_str)


name = 'John'
product_name = 'rice'
price = 22.3456

message = f'Hello {name}! You have bought {product_name} at ${price:.2f}'
print(message)


name = name + ' ' + 'Deere'
print("The name is: ", name)

# list

my_list = [1, 2, 3, 4]
my_list[0] = 99
print("My list: ", my_list)
print("The length of my list is:", len(my_list))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My list is:", my_list)

print("List from index 4:", my_list[4:])

my_second_list = list(my_list)
my_list[0] = 100
print("My list:", my_list)
print("My second list:", my_second_list)

print("My list sorted: ", sorted(my_list))
print("My list: ", my_list)

second_list = [11, 12, 13]
my_list.append(second_list)
print("My list with append: ", my_list)

my_list.extend(second_list)
print("My list with extend: ", my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = tuple(my_list)
print("Mi tuple is: ", my_tuple)

print("Sizeof my list:", my_list.__sizeof__())
print("Sizeof of my tuple: ", my_tuple.__sizeof__())
print("Sizeof list:", [].__sizeof__())
print("Sizeof tuple: ", ().__sizeof__())

person = {
    'name': 'John',
    'age': 32,
    'job': 'clerk',
    'address': None,
    'products': {
        'name': 'Dacia',
        'price': 100
    }
}
person2 = deepcopy(person)
print(person)
print(person['name'])
print(person.get('salary', 0))
print(person.get('address', ''))

for key, value in person.items():
    print(f'{key} -> {value}')

print("Person2:", person2)

my_list = [1, 2, 3, 4, 1, 5, 7, 2]
uniques = list(set(my_list))
print("Uniques: ", uniques)



