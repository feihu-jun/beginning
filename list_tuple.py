#list 和 tuple（不能正常使用append（）和insert（）等 固定的list）的用法05
classmate = ['yi pig','funny yang','sigua','boss huang']#这就是一个list
print (classmate)
print (len(classmate))
print (classmate[2])#索引是从 0 开始的 所以2 是list的第三个
print (classmate[-1])#boss huang 负索引是负顺序的
classmate.append('dad hao')#在list中加一个元素 加到最后
print(classmate)
classmate.insert(0,'feihu')#在list中指定位置加一个元素  还是从0开始
print (classmate)
classmate.pop(5)#删除用pop classmates.pop() 删除指定位置.pop(3)
print (classmate)
classmate[0] = 'dad'#更换指定位置元素
print (classmate)
language = ['python','java',['php','go'],'c','1']#数据类型可以不同,注意只有五个元素
print (language)
a1 = ['php','go']
a2 = ['python','java',a1,'c','1']
print (a1[0],a2[2][0])#通过两种方式拿php
t = (1)
print (t)#定义的不是 tuple，是 1 这个数！因为()既可以表示 tuple，又可以表示数学公式中的小括号
#只有 1 个元素的 tuple 定义时必须加一个逗号,来消除歧义 【不变的是指向】
print (t,)
t = ('a', 'b', ['A', 'B']) #一个"可变"tuple 这里其实还是转变的list
t[2][0] = 'X' 
t[2][1] = 'Y' 
print (t)
input()
