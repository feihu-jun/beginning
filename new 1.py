b = [1,2,3,4]
c = b[0:2]#注意这里不包括第‘2’个元素
c2 = b[:]
print(b)
print(c)
print(c2)
d = b#这里b和d指向了同一实体，改变一个改变了所有
d[0] = 'hi'
b[1] = 3
print(b)
print(c2)#此处是b的一个副本，c2不会有变化！！！

input()