list1 = [1, 2, 3, 4, 5]
print(list1)


def generator_func():
    for i in range(5):
        yield i


gen = generator_func()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
