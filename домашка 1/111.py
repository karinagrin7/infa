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
mv = max(mas)
mn = 0
m = (mv + mn + 1) // 2
mi = len(mas) - 1
ma = 0
while ma != mi:
    m = (mv + mn + 1) // 2
    ma = 0
    mi = 0
    for i in range(len(mas)):
        if mas[i] > m:
            ma += 1
        elif mas[i] < m:
            mi += 1
    print(m, mv, mn, ma, mi)
    if mi > ma:
        mv = m
    elif ma > mi:
        mn = m
print(m)
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
