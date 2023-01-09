print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)

'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = (s2-s1)/s1
print(f'The grades of Ming increased by {r:.1f}%')

classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)

print(len(classmates))
classmates[-1]
print(classmates[-1])
classmates.append('Adam')
classmates.insert(1, 'Jack')
print(classmates.pop(1))
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)
print(len(s))

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')   

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('old')
else:
    print('young')

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    if n > 10: 
        break 
    print(n)
    n = n + 1
print('END')
3023

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Bob')
print(d)

s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])
s.add(4)
print(s)
s.remove(4)
print(s)
