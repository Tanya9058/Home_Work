my_list = [1, 2, 3, 1]

my_dict = {k: my_list.count(k) for k in my_list if my_list.count(k) > 1}

if len(my_list) == len(set(my_list)):
    print('Список состоит из уникальных элементов')
else:
    print(f'Список содержит повторяющиеся элементы: {my_dict}')


