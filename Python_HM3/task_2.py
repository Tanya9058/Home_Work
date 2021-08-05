import itertools

a = '123456789'
new = []
for i in a:
    new.append(i)
    for j in list(range(int(i) + 1, len(a) + 1)):
        i += str(j)
        new.append(i)


all_numbers = []
s = 0
e = 9
k = 0
while len(all_numbers) < 9:
    all_numbers.append(new[s:e])
    k += 1
    e += 9 - k
    s += 9 - k + 1

for i in all_numbers:
    print(i)

one = ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789']
res = list(itertools.combinations(one,2))
print(res)
# st = ''
# for i in all_numbers:
#     for j in i:
#


print(all_numbers)


