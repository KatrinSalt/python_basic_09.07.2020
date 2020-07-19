# функции
def my_sum(a, b):
    result = a + b
    return result


m = my_sum(3, 6)
print(m)


def my_map(func, iter_object):
    result = []
    for itm in iter_object:
        result.append(func(itm))
    return result
