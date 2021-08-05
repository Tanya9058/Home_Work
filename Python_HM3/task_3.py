numbers = [61, 228, 9]

numbers_str = [str(i) for i in numbers]
numbers_str.sort(reverse=True)
print(numbers_str)
result = int(''.join(numbers_str))
print(result)




