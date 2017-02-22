def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(4, 4))
print(power(2, 3))
def power(x, n=2 ):#选参数在前，默认参数在后多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(4))
print(power(2))
print(power(4, 3))
