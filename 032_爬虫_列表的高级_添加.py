#_*_coding : utf-8 _*_
#@Time : 2022/5/11 16:06
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# append  追加   在列表的最后来添加一个对象/数据
food_list=['铁锅炖大鹅','酸菜五花肉']
print(food_list)

food_list.append('小鸡炖蘑菇')
print(food_list)

# insert   插入
char_list=['a','b','d']
print(char_list)
# index的值就是你想插入数据的那个下标
char_list.insert(3,'c')
print(char_list)

#extend
num_list=[1,2,3]
num1_list=[4,5,6]

num_list.extend(num1_list)
print(num_list)
