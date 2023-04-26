from inspect import isgenerator


def some_gen(begin, max_count, func):
    count = 0
    while count < max_count:
        yield begin
        begin = func(begin)
        count += 1


def pow(x):
    return x ** 2


gen = some_gen(2, 4, pow)
assert isgenerator(gen) is True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

