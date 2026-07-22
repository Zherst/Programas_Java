ct = 0
ma=0
me=0
cn=0
na=0
while True:
    n = int(input('número: '))
    if n == 0:
        break
    if ma == 0:
        ma = n
    if me == 0:
        me == n

    if n % 3 == 0:
        ct = ct + 1
    if n < 0:
        cn = cn + 1
    if n > ma:
        ma = n
    elif n < me:
        me = n
print(ct)
print(ma)
print(me)
print(cn)



