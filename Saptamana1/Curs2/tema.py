# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_list1 = sorted(my_list)
print('my_list:', my_list, 'my_list1:', my_list1)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_list2 = sorted(my_list, reverse=True)
print('my_list:', my_list, 'my_list2:', my_list2)

# afișarea numerelor cu indici pari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_sliced_list_par = my_list[0::2]
print('my_list:', my_list, 'my_sliced_list_par:', my_sliced_list_par)

# afișarea numerelor cu indici impari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_sliced_list_impar = my_list[1::2]
print('my_list:', my_list, 'my_sliced_list_impar:', my_sliced_list_impar)

# afișarea elementelor multipli ai lui 3.

print('my_list:', my_list, end='')
multiples = []

for i in my_list:
    if i % 3 == 0:
        multiples.append(i)

print(' multiples of 3: ', multiples)



