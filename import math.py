import math #import math 语句表示导入 math 包，并允许后续代码引用 math包里的 sin、cos 等函数
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)#横坐标变换
    ny = y - step * math.sin(angle)#纵坐标变换
    return nx, ny
print('\n'*3)
print(move(2, 4, 3, angle=4))
print(move(4, 1, 2, angle=0))
x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)#Python 的函数返回多值其实就是返回一个 tuple，但写起来更方返回一个 tuple 可以省略括号
print(x, y)#返回一个 tuple 可以省略括号？
print(r)
from abstest import my_abs #用from abstest import my_abs来导入my_abs()函数
print(my_abs(-3))

