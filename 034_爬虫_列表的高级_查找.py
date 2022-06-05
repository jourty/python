#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:17
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# in 是判断某个元素是否在某个列表中
food_list=['锅包肉','白肉','东北乱炖']

# 判断一些控制台输入的那个数据是否在列表中

food=input('请输入您想吃的食物')

if food in food_list:
    print('在')
else:
    print('不在')


    # not  in
ball_list=['篮球','台球']

# 在控制台上输入你喜欢的球类   然后判断是否不在这个列表中
ball=input('请输入您喜欢的球类：')
if ball not in ball_list:
    print('不在')
else:
    print('在')