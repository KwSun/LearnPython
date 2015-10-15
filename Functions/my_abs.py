def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

a = my_abs(-2)
b = my_abs(13.14)
print(a)
print(b)