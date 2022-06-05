#创建一个test.txt文件

# open(文件的路劲，模式)
# 模式  ：w  可写
# r：可读
open('test.txt','w')

# 打开文件以及写入数据
fp=open('test.txt','w')
fp.write('hello  world')


