
# 使用函数来计算1和2的和

def sum(a,b):
    c=a+b
    print(c)

# 位置参数  按照位置一一对应的关系来传递函数
sum(1,2)

# 关键字传参
sum(a=100,b=200)

# 在定义函数的时候 sum(a,b)  我们称a和b为形式参数    简称形参
#调用函数的时候    sum(1,2)  我们称1和2为实际参数   简称实参