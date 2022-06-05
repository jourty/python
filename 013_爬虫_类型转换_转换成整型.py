#_*_coding : utf-8 _*_
#@Time : 2022/4/24 10:37
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

#类型转换
#str  -->int
a='123'
print(type(a))
print(int(a))

#float   -->int
b=1.63
print(type(b))
#如果我们将float转为整型   那么会返回的是一个小数点前面的数据
c=int(b)
print(c)
print(type(c))

#boolean  -->int
#强制类型转换为谁  就写什么方法
# True   --->1   False ---->0
d=False
print(type(d))
f=int(d)
print(f)

#123.456 和12ab 字符串，都包含非法字符，不能被转换成为整数 ，会报错
# str='1.23'
# print(type(str))
# str1=int(str)
# print(str1)


