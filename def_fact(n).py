#递归函数\
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(4))#。理论上，所有的递归函数都可以写成循环的方式
print(fact(100))
#print(fact(1000)) 小心栈溢出，进入一个函数栈加一。函数返回，栈就会减一层栈帧
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)#？？？
#多数编程语言没有针对尾递归做优化，Python 解释器也没有做优化，所以，即使把上面的 fact(n)函数改成尾递归方式，也会导致栈溢出。