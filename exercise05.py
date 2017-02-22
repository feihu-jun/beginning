#exercise05
#小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）
#帮小明计算他的 BMI 指数，并根据 BMI 指数： 
# 低于 18.5：过轻 
# 18.5-25：正常 
# 25-28：过重 
# 28-32：肥胖 
# 高于 32：严重肥胖
height = 1.75 
weight = 180.5 
bmi = weight/(height*height)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi <=25:
    print('正常')
elif 25 <= bmi <=28:
    print('过重')
elif 28 <= bmi <=32:
    print('肥胖')
else:
    print('严重肥胖')
input()