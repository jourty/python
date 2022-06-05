#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:54
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# 定义一个字典
person={'name':'吴倩','age':29}

# 访问person的name
print(person['name'])
print(person['age'])

# 使用[]的方式获取字典中不存在的key的时候   会发生异常   keyerror
# print(person['sex'])

# 不能使用.的方式来访问字典的数据
# print(person.name)

print(person.get('name'))
print(person.get('age'))

# 使用.的方式，获取字典中不存在的key的时候   会返回None值
print(person.get('sex'))