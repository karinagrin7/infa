"""def fact(x):
    if x==1:
        return 1
    return x * fact(x - 1)

print(fact(5))

def fact_it(x):
    res=1
    for i in range(2,x+1):
        res= res*i
        return res

print(fact(5))

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(1))
print('c')
print('cc')
print('ccc')
print('cccc')
print('ccc')
print('cc')
print('c')
n, c= input().split(" ")
n= int(n)

import numpy as np
x = np.array([1,2,3,4])
y = np.array([1,2,3,5])
print(x*y)
"""

'''
s = input()
print(s)
b = len(s)
for i in range(b//2):
    if s[i] != s[b - i - 1]:
        print('NO')
        break
    print('YES')
'''
"""
#4
mas = list(map(int, input().split()))
for i in range(1, len(mas), 2):
    mas[i], mas[i - 1] = mas[i - 1], mas[i]
print(*mas)
"""
"""
mas = list(map(int, input().split()))
print(mas[1:6])
"""
#5
mas = list(map(int, input().split()))
print(mas[-1], *mas[:-1])