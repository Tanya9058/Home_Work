my_string = 'abc83 cde7 1 b 24'

result_list = []
st = ''
for i in my_string:
    if i.isdigit():
        st = st + i
    else:
        if st != '':
            result_list.append(int(st))
            st = ''
if st != '':
    result_list.append(int(st))

print(result_list)


