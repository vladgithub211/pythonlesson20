def gen():
      yield
      print("Первый перебор")
      yield
      print("Второй перебор")
y = gen()
print(next(y))
print(next(y))
print(next(y))
        
