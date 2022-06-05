#_*_coding : utf-8 _*_
#@Time : 2022/5/11 15:14
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫







# 一个一个的输出  叫做循环 也叫遍历


# for    格式：for  变量  in  要遍历的数据：
#                方法体
# 循环字符串
s='china'
for i in s:
    print(i)


#     range（5）
# range方法的结果  一个可以遍历的变量
#   左闭右开区间
for i in range(5):
    print(i)


    # range(1,6)
    # range(起始值,结束值)
#     左闭右开区间
for i in range(1,6):
    print(i)

    # range(1,10,3)
# range(起始值,结束值,两数直接相差值)
#     左闭右开区间
for i in range(1,10,3):
    print(i)


    # 应用场景  会爬取一个列表返回给我们
    # 循环一个列表
a_list=['周杰伦','林俊杰','陶喆']
#     遍历列表中的元素
for i in a_list:
    print(i)

#     遍历列表中的下表

# 判断列表中的元素的个数
print(len(a_list))

for i in range(len(a_list)):
    print(i)