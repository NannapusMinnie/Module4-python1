'''
input x
if x is an even number, print('A')
if x is even and isn't divisible by 3, print('B')
if x is even and divisible by 3, print('C')
if x is odd print('D')
'''

''' x = float(input())
if x % 2 == 0 and not x % 3 == 0:
    print('B')
elif x % 2 ==0 and x % 3 == 0:
    print('C')
else:
    print('D') '''

x = float(input())

if x % 2 == 0:
    if x % 3 != 0:
        print('B')
    else:
        print('C')
else:
    print('D')


