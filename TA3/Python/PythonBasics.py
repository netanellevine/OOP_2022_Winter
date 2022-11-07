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
