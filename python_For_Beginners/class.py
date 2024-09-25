
class CuteCat:
    def __init__(self,cut_name,cat_age,cat_color):
        self.name = cut_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print("喵" * self.age)

    def think(self,content):
        print(f"小猫{self.name}在思考{content}……")


cat1 = CuteCat("小可爱",3,"红色")

# print(cat1.name,"的年龄是",cat1.age ,"，花色是",cat1.color)

print(f"猫咪{cat1.name}的年龄是{cat1.age} ，花色是{cat1.color}")
cat1.speak()
cat1.think("现在去抓铲屎官还是去睡觉")

