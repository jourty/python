#_*_coding : utf-8 _*_
#@Time : 2022/5/11 14:14
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫

# and短路与    性能优化
a=36
a>10 and print('hello world')
# and的性能优化  当and前面的结果是false的情况下  那么后面的代码就不用再执行了
a<10 and print('hello world')

# or短路或      性能优化  只要有一方为true  那么结果就是true
a>10 or print('你好世界')
a<10 or print('你好世界')
