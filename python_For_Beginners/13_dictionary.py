﻿# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序

slang_dict = {"凡尔赛":"指通过一些反向的表述来透露自己的优越生活的人。",
              "打工人":"指对所有从事体力劳动或者技术劳动的人的统称。"}
slang_dict["赘婿吉吉国王"] = "指因热播电视剧《赘婿》中扮演苏文兴的刘冠麟有个镜头和动画《熊出没》中吉吉国王表情很相似，而被网友们称为“赘婿吉吉国王”。"
slang_dict["集美"] = "指好姐妹，来源于抖音主播迷人的郭老师。她的口头禅就是姐妹们。"
slang_dict["U1S1"] = "指有一说一，实话实说。U1S1是字母与数字的谐音缩写，大多数是用来网友在网站下面评论等，加上U1S1，似乎自己的观点更有说服力。"
slang_dict["逆行者"] = "指反向行走的人，常用于称呼面对危难挺身而出的强者，如抗击新冠肺炎疫情中最美“逆行者”。平凡中涌现的无数“逆行者”，用生命守护生命，深刻诠释着新时代英雄精神的内涵。"
slang_dict["工具人"] = "指被对方当工具使唤，对他人任劳任怨付出却得不到平等的对待。"
slang_dict["懂王"] = "指没有人比我更懂，别人都是错的，只有自己是对的，就自己最懂。"
slang_dict["爷青回"] = "是“爷的青春又回来了”的缩写，用来表达人在变化后的环境中面对曾经熟悉的人和事物时，油然而生的一种喜悦之情。"
slang_dict["真香"] = "意思是打脸。这个梗的由来是《变形记》。其中有一期的城市主人公去了乡村后，发誓不吃乡村家庭的蛋炒饭，后来又吃了，并说“真香”。"

query = input("请输入您要查询的流行语：")
if query in slang_dict:
    print("您查询的“" +  query  + "”含义如下" )
    print(slang_dict[query])
else:
    print("抱歉，您查询的流行语暂未收录，感谢理解。")
    print("当前本词典已收录" + str(len(slang_dict)) + "条。")
# ###########
total = 0
for i in range(1,101):
    total = total + i
print(total)