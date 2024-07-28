from datetime import datetime
from wxauto import WeChat
import time
# 导入openai
from openai import OpenAI

# 获取微信窗口对象
wx = WeChat()
# 获取OpenAI对象
client = OpenAI()

listen_list = [
    'WeChatGPT2.0'
]

for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)

wait = 1  # 设置1秒查看一次是否有新消息
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who              # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)   # 获取消息内容
        # 回复收到
        for msg in one_msgs:
            current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msgtype = msg.type       # 获取消息类型
            content = msg.content    # 获取消息内容，字符串类型的消息内容
            # print(f'【{who}】：{content}')
        # ===================================================
        # 处理消息逻辑（如果有）
        # 
        # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
        # 
        # ===================================================
        
            # 如果是好友发来的消息（即非系统消息等），则回复收到
            if msgtype == 'friend':
                print(f'[{current_time_str}] {msg.sender.ljust(12)}：{msg.content}')
                if '@WeChatGPT' in msg.content:
                    valid_msg = msg.content.replace('@WeChatGPT', '')
                    completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {'role': 'system', 'content': '惜字如金，言简意赅'},
                            {'role': 'user', 'content': valid_msg}
                        ]
                        )
                    chat.SendMsg(msg=completion.choices[0].message.content, at=msg.sender)  # 回复
            elif msg.type == 'self':
                None
    time.sleep(wait)
