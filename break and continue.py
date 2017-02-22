#break 和 continue语句07
n = 1
while n <= 100:
    if n > 15:
	    break 
    print(n)
    n = n + 1
print('end')


n = 0#一输入就闪掉 但是代码没问题啊
while n < 10：
    n = n + 1
	if n % 2 == 0：
	    continue# continue语句会直接继续下一轮循环,不执行后面的print
    print(n)
input()