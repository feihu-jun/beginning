#dict (d.get的结果d.opp删除)& set08 
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
k=(names[0],scores[0])
print (names)
print(k)
print('\n')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}#法1初始化时指定
print(d)
print(d['Michael'])
d['Adam'] = 67#dict第二种实现方式，通过key放入
print(d['Adam'])
print('Adam' in d) #用in来判断key是否存在
print(d.get('Thomas'))#返回None的时候Python的交互式命令行不显示结果。
print(d.get('Bob'))#存在时得出了正确结果。d.get
d.pop('Tracy')#删除一个key 用d.opp
print(d)# 注意！dict内部存放的顺序和key放入的顺序是没有关系的。dict的key必须是不可变对象
s = set([1,1,2, 2, 3])#重复元素在set中自动被过滤
print(s)#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
s.add(4)
print(s)
s.remove(1)
print(s)
s1 = set([1, 2, 3])#两个set可以做数学意义上的交集、并集等操作：
s2 = set([2, 3, 4])
print (s1 & s2)
print (s1 | s2)
h = ['c', 'b', 'a']
h.sort()
print(h)
g = 'abc'
print (g.replace('a', 'A'))#字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'
print(g)

input()