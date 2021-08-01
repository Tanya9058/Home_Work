number = input('Enter your number:\n')
even = 0
odd = 0
if number.isdigit():
    for i in number:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Count even numbers: {even}\nCount odd numbers: {odd}')
else:
    print('Wrong format')


