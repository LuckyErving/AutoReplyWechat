# wechat autoreply
import itchat
import requests
import re
# 抓取网页
def getHtmlText(url):
        try:
                r = requests.get(url,timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                return r.text
        except:
                return ""
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    # 当消息不是由自己发出的时候
#     if not msg['FromUserName'] == Name["Jestiao"]:
        # 回复给好友
        url = "http://www.tuling123.com/openapi/api?key=您的小图key&info="
        url = url + msg['Text']
        html = getHtmlText(url)
        testText="fuctest"
        message = re.findall(r'\"text\"\:\".*?\"',testText)
        # reply = eval(message[0].split(':')[1])
        
        reply="Hi, there! I am Eva, assistant of Erving.\nHe is busy struggling with the deadline and preparing the final exams.\
                \nHe will reply you ASAP. Thx for your consideration."
        return reply

if __name__ == '__main__':
#     itchat.auto_login()
    itchat.auto_login(enableCmdQR=2)

    # 获取自己的UserName
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
            Nic.append(friends[i]["NickName"])
            User.append(friends[i]["UserName"])
    for i in range(len(friends)):
            Name[Nic[i]] = User[i]
    itchat.run()
