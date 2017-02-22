#自动给输入姓名的人hello程序01#
name = input ('please enter your name:')
print('\n' * 5)
print('heelo,',name)
print('\n' * 2)#此处可以写成 n=5 | print ('\n'*n) 
input('enter to <close>')#为了解决直接闪退设置的。还可以raw_input() 随机输入的意思。因为python运行完就直接关闭了