import random

print('Week 2')

is_ok = True
while is_ok:
    print('Hello World!!')
    is_ok = False

for i in range(10): # merge de la 0 si se opreste la n-1
    print(i+1, end=' ')

choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n')
while True:
    random_choice = random.choice(choices)
    if random_choice % 3 == 0:
        break
    print(random_choice)


print(f'rand_choice={random_choice}')

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

print('\n\n\n\n\n\n\n')

name = 'John'

if name == 'John':
    print('Hello John')
else:
    pass


print('\n\n\n')

def print_week():
    print('Week 2')

def get_sum(a, b):
    return a + b

print(print_week())

sum = get_sum(1,2)
print(f'Suma e: {sum}')

print('\n\n\n')
def print_greetings(first_name, last_name, age, address='', phone_number='', email_address=''):
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Age: {age}')
    print(f'Address: {address}')
    print(f'Phone Number: {phone_number}')
    print(f'Email Address: {email_address}')

print_greetings('John', 'Doe', 40, phone_number='0755214232')

print('\n\n\n')

my_string = 'https://docs.python.org/3/library/exceptions.html'
my_var = 0 #input("Please introduce a number: ")
try:
    my_int = int(my_var)
    my_double = my_int*2
except ValueError as e:
    print('The value is invalid!!')
except NameError as e:
    print('Name error was triggered!!')
else:
    print('The value is doubled: ', my_double)
finally:
    print('This code is always executed!')
print('\n\n\n\n')

print(dir(__builtins__))

print('\n\n\n')

name = 'Valentin'

def my_func():
    name = 'Valentin - local'
    print(name)

print(name)
my_func()
print(name)

a = 'a'

#def my_function():
    #print(f'my second function {msg}')
        