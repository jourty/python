#_*_coding : utf-8 _*_
#@Time : 2022/4/24 11:05
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

#整数转换为布尔类型时，负数与正数都为True
a=1
print(type(a))
b=bool(a)
print(b)
print(type(b))

c=2
print(type(c))
d=bool(c)
print(d)
print(type(d))

f=-1
print(type(f))
e=bool(f)
print(e)
print(type(e))

i=0
print(type(i))
#在整数中0强制转换为布尔类型时返回为False
j=bool(i)
print(j)
print(type(j))

#浮点数
#将浮点数转换为布尔类型数据的时候，整的浮点数与负的浮点数的结果是True
#如果是0.0  那么结果是false
# v=1.0
# print(type(v))
# n=bool(v)
# print(n)
# print(type(n))

# v=-1.0
# print(type(v))
# n=bool(v)
# print(n)
# print(type(n))

v=0.0
print(type(v))
n=bool(v)
print(n)
print(type(n))
#字符串
#只要字符串中有内容  那么在强制类型转换为bool的时候  那么就返回True
# x='哦豁'
# print(type(x))
# y=bool(x)
# print(y)
# print(type(y))

# x=' '
# print(type(x))
# y=bool(x)
# print(y)
# print(type(y))

x=''
print(type(x))
y=bool(x)
print(y)
print(type(y))
#列表
#只要列表中有数据  那么强制类型转换为bool的时候  就返回True
# h=['a','b','c']
# print(type(h))
# k=bool(h)
# print(k)
# print(type(k))
# 如果列表中什么数据类型都没有的情况下  那么返回的是False
h=[]
print(type(h))
k=bool(h)
print(k)
print(type(k))
#元组
# 只要元组中有数据  那么强制类型转换为bool的时候  就返回True
# l=('a','b')
# print(type(l))
# m=bool(l)
# print(m)
# print(type(m))
# 如果元组中什么数据类型都没有的情况下  那么返回的是False
l=()
print(type(l))
m=bool(l)
print(m)
print(type(m))
#字典

