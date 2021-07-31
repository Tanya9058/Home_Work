my_string = 'abc83 cde7 1 b 24'
my_list = my_string.split(' ')
result_list = []

for i in my_list:
    if i.isdigit() is True:
        result_list.append(i)
    # else:

print(result_list)
