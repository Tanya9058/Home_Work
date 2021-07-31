information = 'Language Python is an interpreted high-level general-purpose programming language'
information = information.lower()
information_list = information.split(' ')

res_count = {i: information_list.count(i) for i in information_list}
res_length = {i: len(i) for i in information_list}

for k, v in res_count.items():
    if v == max(res_count.values()):
        print(f'Most consumed word:\n {k}: {v}')

for k, v in res_length.items():
    if v == max(res_length.values()):
        print(f'Most characters in a word:\n {k}: {v}')