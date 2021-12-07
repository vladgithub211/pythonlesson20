def gen(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a = b
        b = a+b
n = int(input("Введите кол-во чисел Ф="))
y = gen(n)
print(next(y))
