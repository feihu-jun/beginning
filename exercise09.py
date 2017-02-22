#请定义一个函数 quadratic(a, b, c)，接收 3 个参数，返回一元二次方程：
#ax2 + bx + c = 0 的两个解。
#提示：计算平方根可以调用 math.sqrt()函数
import math
def quadratic(a, b, c):
    dert = b * b -4*a * c
    if dert >= 0:
        x1 = (-b + math.sqrt(dert)) / (2 * a)
        x2 = (-b - math.sqrt(dert)) / (2 * a)
        return x1, x2  # 返回值是一个 tuple！！！
    else:
        print('no reault')#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

print(quadratic(1, 2, 1))
print(quadratic(3, 3, 2))
