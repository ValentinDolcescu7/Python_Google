"""Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
numere întregi sau reale.
○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
○ your_function() va returna 0.
○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
"""


def your_function(*args, **kwargs):
    total_sum = 0

    for value in args:
        if isinstance(value, (int, float)):
            total_sum += value

    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total_sum += value

    return total_sum

# Exemple de utilizare
print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))  # va returna 3
print(your_function())  # va returna 0
print(your_function(2, 4, 'abc', param_1=2))  # va returna 6


"""Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:
○ suma totală a numerelor
○ suma numerelor pare
○ suma numerelor impare
"""
def sum_recursively(lst, total_sum=0, even_sum=0, odd_sum=0):
    if not lst:
        return total_sum, even_sum, odd_sum

    current_value = lst[0]

    if current_value % 2 == 0:
        even_sum += current_value
    else:
        odd_sum += current_value

    total_sum += current_value

    return sum_recursively(lst[1:], total_sum, even_sum, odd_sum)


# Exemplu de utilizare
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total, even, odd = sum_recursively(numbers)
print(f"Suma totală: {total}")
print(f"Suma numerelor pare: {even}")
print(f"Suma numerelor impare: {odd}")



"""Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
valoarea 0.
"""
def read_integer_from_keyboard():
    try:
        value = int(input("Introduceți un număr întreg: "))
        return value
    except ValueError:
        return 0

# Exemplu de utilizare
result = read_integer_from_keyboard()
print(f"Valoarea citită: {result}")
