#if判断06
age = 18
if age < 18:
    print('teenager')
elif age > 18:
    print('adult')
else:
    print('just only adult')	
x = input('brith:')
s = int(x)#input()返回的数据类型是str,str不能直接和整数比较,必须先把str转换成整数 int
if s > 2000:#这块怎么判断是布尔值
    print('00后')
else:
    print('not 00 后')
input()