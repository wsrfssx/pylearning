from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling = Tuling(api_key='c3d02c6c14a84fedb1a9cfcd6cff4479')


# 自动回复所有文字消息
#@bot.register(msg_types=TEXT)
#def auto_reply_all(msg):
#    tuling.do_reply(msg)

my_friend = ensure_one(bot.search('青青草'))
# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

# 开始运行
bot.join()

