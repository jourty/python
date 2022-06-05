#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:32
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

a_tuple=(1,2,3,4)

print(a_tuple[0])
print(a_tuple[3])

# 元组是不可以修改里面的内容的
# a_tuple[3]=5
# print(a_tuple)

a_list=[1,2,3,4]
a_list[3]=5
print(a_list)
# 列表中的元素是可以修改的

a_tuple=(5)
print(type(a_tuple))

# 当元组中只要一个元素的时候   那么它是整型数据
# 定义只有一个元素的元组   需要在唯一的元素后面写一个逗号
b_tuple=(5,)
print(type(b_tuple))

