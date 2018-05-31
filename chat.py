## -*- coding: utf-8 -*-
import itchat
import requests
import random
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': '7325fdc08bf74400bceb37eb90e17eab',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)
#def print_content(msg):
#    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    defaultReply = 'I received: ' + msg['Text']
    num= random.randint(1,10)
    print(num)
    if num==1:
        x='老子跟你说哦，'
    elif num==2:
        x='妈了个逼,'
    elif num==3:
        x= '傻逼我跟你说，'
    elif num==4:
        x='儿砸，'
    elif num== 5:
        x='爸爸告诉你，'
    elif num== 6:
        x='叮叮叮，咚咚咚，登登等登瞪瞪,'
    elif num== 7:
        x='操你妈,'
    elif num==8:
        x='妈了个逼，'
    else:
        x= '你是傻逼吗,'
    reply = x + get_response(msg['Text'])
    return reply or defaultReply
itchat.auto_login(enableCmdQR=True)
itchat.run()