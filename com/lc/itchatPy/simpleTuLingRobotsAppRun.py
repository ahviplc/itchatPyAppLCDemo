#coding=utf8
import requests

apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key'    : '71f28bf79c820df10d39b4074345ef8c', # 如果这个Tuling Key不能用，那就换一个
    'info'   : 'hello', # 这是我们发出去的消息
    'userid' : 'wechat-robot', # 这里你想改什么都可以
}
# 我们通过如下命令发送一个post请求
r = requests.post(apiUrl, data=data).json()

# 让我们打印一下返回的值，看一下我们拿到了什么
print(r)