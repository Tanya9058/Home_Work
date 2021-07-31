my_dict = {'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000, 'f': 2000, 'g': 400}

val_list = [i for i in my_dict.values() if type(i) != str]
val_list = list(set(val_list))
val_list.sort(reverse=True)
val_new_list = val_list[:3]

for i in val_new_list:
    for k, v in my_dict.items():
        if i == v:
            print(f'{k}: {i}')