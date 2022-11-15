# Data types:
this_is_int = 5
print(this_is_int)
print(type(this_is_int))
print()

this_is_float = .4
print(this_is_float)
print(type(this_is_float))
print()

this_is_string = 'Hello'
print(this_is_string)
print(type(this_is_string))
print()

this_is_bool = True
print(this_is_bool)
print(type(this_is_bool))
print()

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Arithmetic operators:
x = this_is_int + this_is_int
print(x)

x = this_is_int * this_is_int
print(x)

x = this_is_int ** this_is_int
print(x)

x = this_is_int / this_is_int * 2
print(x)

x = this_is_int / (this_is_int * 2)
print(x)

x = this_is_int // (this_is_int * 2)
print(x)

x = this_is_int % (this_is_int * 2)
print(x)

x = this_is_int * this_is_int
print(float(x))

x += this_is_int
print(float(x))

x -= this_is_int
print(float(x))
print()

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Logical operators:
print(x == 25)
print(x > 25)
print(x < 25)
print(x >= 25)
print(x <= 25)
print(not x == 25)
print(x == 25 and x == 25.1)
print(x == 25 or x == 25.1)
print(x == 25 or x == abs(25.1))
print()

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Conditions:
a = 10
b = 20
if a >= b:
    print('a is bigger!')
else:
    print('b is bigger!')

a = [1, 2, 3, 4, 5]
if 5 in a:
    print(f'5 is in a -> {a}')
    print(5, 'is in a ->', a)
    print('5 is in a -> {}'.format(a))
if type(a[3]) is float:
    print(f'a[3]={a[3]} which is an float!')
elif type(a[3]) is str:
    print(f'a[3]={a[3]} which is an str!')
else:
    print(f'a[3]={a[3]} which is an integer!')

if a[3] > 3: print("Yay!")
print("Yay!") if a[2] > 3 else print("Nay!")
print()

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Loops:
i = 0
for i in range(len(a)):
    print(a[i])

for num in a:
    print(num)

i = 0
while i < len(a):
    print(a[i])
    i += 1

a = [i for i in range(5)]
print(a)

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Lists
arr = [1, 2, 3, 4, 5]
print(arr)
arr = ['This', 'is', 'Python']
print(arr)
arr = [True, 3, 'Hello', (5, 3, 2), [1, 2, 3]]
print(arr)
for i in arr:
    print(type(i))

print(len(arr))
arr.append(6)
arr[-1] = 5
arr.insert(3, "Hi")
print(arr)
print(arr.pop())  # == arr.pop(-1)
print(arr.pop(3))
arr.reverse()
print(arr)
print(arr.index(3))
# print(arr.index(0))  # Will throw a ValueError
print(arr.count(0))
arr.remove(3)
print(arr)

a = [1, 2, 3, 4, 5]
print(a[0])
print(a[-1])
print(a[-2])
# print(a[6])  # Will throw a IndexError
print(a[:3])
print(a[1:4])
print(a[2:])
b = [6, 7, 8, 9, 10]
c = a + b
print(c)
a.extend(b)
print(a)

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Tuples
tup = (1, 2, 3)
print(tup, type(tup))
# tup[2] = 10  # Will throw a TypeError because tuple is immutable
print(tup)
a, b, c = tup
print(a, b, c)
tup *= 5
print(tup)

print('_____________________________________________________________________________________')
print('_____________________________________________________________________________________')

# Dictionaries
this_dict = {1: 'This', 2: 'is', 3: 'a', 4: 'dictionary'}
this_dict[5] = '!'
print(this_dict)
this_dict = {1: 'This', 2: 'is', 3: 'a', 4: 'dictionary', 5: '!', 5: '!!!'}
print(this_dict)  # Only one of them will be obtained

# Access
print(this_dict[3])
print(this_dict.get(2))

# Remove
this_dict.pop(5)
print(this_dict)

keys = this_dict.keys()
print(keys)
values = this_dict.values()
print(values)

print(this_dict.items())

for k, v in this_dict.items():
    print('Key ->', k, 'Value ->', v)


