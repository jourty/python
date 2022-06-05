#_*_coding : utf-8 _*_
#@Time : 2022/5/11 15:39
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# 获取字符串长度  len  length缩写  长度
s='china'
print(len(s))

# 查找内容：find    查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现位置
s1='china'
print(s1.find('a'))

# 判断：startswith/ endswith            判断字符串是不是以谁谁开头/结尾
s2='china'
print(s2.startswith('c'))
print(s2.endswith('n'))

# 计算出现次数：count  a出现3次
s3='aaabb'
print(s3.count('a'))

# 替换内容：replace    替换字符串中指定的内容，如果指定次数count，则替换不会超过count次
s4='cccddd'
print(s4.replace('c','d'))

# 切割字符串：split    通过参数内容切割字符串
s5='1#2#3#4'
print(s5.split('#'))

# 修改大小写：upper，lower    将字符串中大小写互换
s6='china'
print(s6.upper())

s7='CHINA'
print(s7.lower())

# 空格处理：strip   去空格

s8='     a    '
print(len(s8))

print(len(s8.strip()))

# 字符串拼接：join    字符串拼接   输出结果 ： haealalao
s9='a'
print(s9.join('hello'))
