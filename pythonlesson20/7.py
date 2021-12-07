b = (2,4,18,26)
def gen():
    for i in b:
        yield i
    y = gen()
    g = 0
while g<len(b):
    print(next(y))
    g = 0
