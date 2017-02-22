def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())#注意这里变了。因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):#多少次，都不会有问题：
    if L is None:
        L = []
        L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end([2, 1, 3]))