#
def f1(a, b, c=0, *args, **kw):#*args 是可变参数，args 接收的是一个 tuple； **kw 是关键字参数，kw 接收的是一个 dict
    print('a =', a, 'b=', b, 'c =', c, 'args=', args,  'kw=', kw)
def f2(a, b, c=0, *, d, **kw):#定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw )
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99)
args = (1, 2, 3, 4)#通过一个 tuple 和 dict，你也可以调用上述函数：
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)