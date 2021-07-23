n = int(input())
# кол-во столбов
m = int(input())
# высота деревьев
h = int(input())
if n == h:
    z = n * m
    c = z / h
    print (c, ' кол-во деревьев ')

if n < h :
    z = n * m
    x = z / h
    if x == int(x):
        c = x + 1
        print (c, ' кол-во деревьев ')
    else:
        print(' проверьте значения ')

else:
    print(' проверьте значения ')

if 1>=m>=100:
    print(' проверьте значения ')

