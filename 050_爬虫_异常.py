#_*_coding : utf-8 _*_
#@Time : 2022/5/31 21:06
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫
#
# 异常的格式
# try：
#     可能出现异常的代码
# except  异常的类型
#      友好的提示

try:
    fp=open('text.txt','r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级，请稍后再试…………')