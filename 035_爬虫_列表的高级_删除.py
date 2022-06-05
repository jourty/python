#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:25
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

a_list=[1,2,3,4,5]

print(a_list)

#根据下标来删除列表中的元素
# 爬取的数据有个别的数据是我们不想要的时候
del a_list[2]
print(a_list)

b_list=[1,2,3,4,5]
print(b_list)

# pop是删除列表中的最后一个元素
b_list.pop()
print(b_list)

#
c_list=[1,2,3,4,5]
print(c_list)

# remove   根据元素来删除列表中的数据
c_list.remove(3)
print(c_list)