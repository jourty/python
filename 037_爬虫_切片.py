#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:40
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

s='hello world'
# 在切片中直接写一个下标
print(s[0])

#左闭右开区间   包含坐标的数据   不包含右边的数据
print(s[0:4])

# 是从起始的值开始   一直到末尾
print(s[1:])

# 是下标为0的索引的元素开始   一直到第二参数为止  遵循左闭右开区间
print(s[:4])

# hello  world
# 从下标为0的位置开始  到下标为6 的位置结束   每次增长2 个长度
print(s[0:6:2])