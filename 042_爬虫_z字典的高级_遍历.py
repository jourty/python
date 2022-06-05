#_*_coding : utf-8 _*_
#@Time : 2022/5/11 17:25
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

#遍历   就是数据一个一个的输出
person={'name':'阿玛','age':18,'sex':'男'}

# 遍历字典的key
# 字典.keys()方法  获取字典中所有的key值
for key in person.keys():
    print(key)


# 遍历字典的value
# 字典.value()方法  获取字典中所有的value值
for value in person.values():
    print(value)

# 遍历字典的key和value
for key,value in person.items():
    print(key,value)

#     遍历字典的项/元素
for item in person.items():
    print(item)



