#默认参数的用法
def enroll(name, gender, age=6,city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('yizhu', 'f')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')#不按顺序提供部分默认参数
def calc(number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum
print(calc([1, 2, 3, 4]))
def calc1(*numbers):#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc1(1, 4))
print(calc1())#numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
nums = [1, 2, 3]
print(calc1(2))
print(calc1(nums[0], nums[1], nums[2]))#1=4=9
print(calc1(*nums))#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
