#循环for x in xx： while： 07
names = ['funyyang','pig yi','sigua','bosshuang','feihu']
for name in names:# for x in ...循环就是把每个元素代入变量 x，然后执行缩进块的语句。 
    print('遍历名为',name)
print('\n'*3)
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x 
print('1-10的和为:',sum)
print('\n'*3)
j = list(range(101))
print('这就是list加range显示0-100',j)
print('\n')
sum = 0
for x in range(101):
    sum = sum + x
print('用循环得出发1-100的和',sum)
print('\n'*2)
sum = 0
n = 100
while n >= 0:
    sum = sum + n
    n = n - 2
print ('偶数之和',sum)

input()