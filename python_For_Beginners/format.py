# 律回春渐，新元肇启。
# 新岁甫至，福气东来。
# 金X贺岁，欢乐祥瑞。
# 金X敲门，五福临门。
# 给XX及家人拜年啦！
# 新春快乐，X年大吉！
from cgi import print_form

name = "老李"
year = "鸡"
message_countent = f"""
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐,{name}年大吉！
"""
# .format(receiver_name = name ,current_year = year )

print(str(message_countent))


gpa_dict = {"老李":4.5,"老王":1.234,"劳达":2.45,
            "小花":1.44542,"达摩":2.3333,}
for name,gap in gpa_dict.items():
    gpa = gpa_dict[name]
    # print("{0}你好，你的当前绩点为：{1:.2f}".format(name,gpa))
    print(f"{name}你好，你的当前绩点为：{gap:.1f}")