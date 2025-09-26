"""
#3
s = input()
print(s)
b = len(s)
for i in range(b//2):
    if s[i] != s[b - i - 1]:
        print('NO')
        break
    print('YES')

#4
mas = list(map(int, input().split()))
for i in range(1, len(mas), 2):
    mas[i], mas[i - 1] = mas[i - 1], mas[i]
print(*mas)


#5
mas = list(map(int, input().split()))
print(mas[-1], *mas[:-1])

#6
mas = list(map(int, input().split()))
for i in range(len(mas)):
    if mas.count(mas[i]) == 1:
        print(mas[i], end=' ')


#7
mas = list(map(int, input().split()))
maxi = 0
max_i = 0
for i in range(len(mas)):
    if mas.count(mas[i]) > maxi:
        maxi = mas.count(mas[i])
        max_i = mas[i]
print(max_i)
"""
#8
mas = list(map(int, input().split()))
for m in range(min(mas), max(mas) + 1):
    mi = 0
    ma = 0
    for i in range(len(mas)):
        if mas[i] > m:
            ma = ma + 1
        elif mas[i] < m:
            mi += 1
    if mi == ma:
        print(m)
        break



"""
#9
f = open('input.txt')
s = f.read()
mas = s.split()
print(mas)
cnt = 0
rd = '.!?'
for i in range(len(mas)):
    if mas[i][-1] in rd:
        cnt += 1
print(cnt) 
"""
