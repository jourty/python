#_*_coding : utf-8 _*_
#@Time : 2022/6/1 22:37
#@Author :Lime
#@File : {NAME}
#@Project : python爬虫
import urllib.request

url='https://www.baidu.com'

# url 的组成
# https://www.baidu.com/s?wd=周杰伦

# https/http      www.baidu.com    443/80     s      wd=周杰伦    #
#  协议               主机             端口      路径      参数       锚点
# http     80
# https     443
# mysql     3306
# oracle     1521
# redis      6379
# mongodb     27017



headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

# 因为urlopen方法中不能存储字典   所以headers不能传递进去
# 请求对象的定制
# 注意   因为参数顺序的问题   不能直接写url  和headers   中间还有date   所以我们需要关键字传参
request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content=response.read().decode('utf8')

print(content)