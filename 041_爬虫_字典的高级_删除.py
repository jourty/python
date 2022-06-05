#_*_coding : utf-8 _*_
#@Time : 2022/5/11 17:13
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# 删除字典中指定的某一个元素
person={'name':'张三','age':18}

# # 删除之前
# print(person)
#
# del person['age']
#
# # 删除之后
# print(person)
#


# # 删除整个字典
# # 删除之前
# print(person)
#
# del person
#
# # 删除之后
# print(person)


# 清空字典  但是保留字典对象
print(person)

# 清空指的是将字典中所有的数据  都删除   而保留字典的结构
person.clear()

print(person)