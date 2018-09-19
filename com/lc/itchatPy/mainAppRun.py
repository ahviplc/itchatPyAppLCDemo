import itchat
import time

"""

itchat
py27 py35

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。

使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。

当然，该api的使用远不止一个机器人，更多的功能等着你来发现，比如这些。

该接口与公众号接口itchatmp共享类似的操作方式，学习一次掌握两个工具。

如今微信已经成为了个人社交的很大一部分，希望这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。


项目简介 - itchat-文档
https://itchat.readthedocs.io/zh/latest/

littlecodersh/ItChat: A complete and graceful API for Wechat. 微信个人号接口、微信机器人及命令行微信，三十行即可自定义个人号机器人。
https://github.com/littlecodersh/itchat


LC 2018年9月19日15:06:11

"""

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

@itchat.msg_register([itchat.content.PICTURE,itchat.content. RECORDING, itchat.content.ATTACHMENT,itchat.content. VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    print( msg['Text'](msg['FileName']))

#OK 输出 下载发过来的附件 都好使 已测试！ LC 2018年9月19日15:31:50

itchat.auto_login(hotReload=True)    #hotReload=True

print("--------------------------------------------------------------------")
print(itchat.search_friends())

# 如果你不想要每次运行程序都扫码，可以在登陆命令中进行设置：
# itchat.auto_login(hotReload=True)




# 命令行二维码
# 通过以下命令可以在登陆的时候使用命令行显示二维码：
# itchat.auto_login(enableCmdQR=True)

itchat.send('Hello, filehelper '+str(time.asctime( time.localtime(time.time()))), toUserName='filehelper')
itchat.send('Message Content ahviplc2代 '+str(time.asctime( time.localtime(time.time()))))
#toUserName：发送对象，如果留空将会发送给自己


"""
# 获取自己的用户信息，返回自己的属性字典
itchat.search_friends()
# 获取特定UserName的用户信息
itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
itchat.search_friends(name='littlecodersh')
# 获取分别对应相应键值的用户
itchat.search_friends(wechatAccount='littlecodersh')
# 三、四项功能可以一同使用
itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')

"""

print(itchat.search_friends(name='ahviplc2代'))



itchat.run()

# 1. 实现微信消息的获取
# itchat的注册时根据类型注册的。
#
# 在获取相应类型的信息时会调用该函数。
#
# 我们现在只需要获取最简单的文本消息，那么只需要这样注册

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
#
# itchat.auto_login()
# itchat.run()