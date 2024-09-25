# 定义一个学生类
# 要求：
# 1.属性包括学生姓名、学号、以及语数英三科成绩。
# 2.能够设置学生科目的成绩。
# 3.能够打印出该学生的所有科目成绩。


class Studnet:
     def __init__(self,st_name,st_num):
         self.name = st_name
         self.num  = st_num
         self.grades = {"语文": 0 , "数学": 0, "英语": 0}

     def set_grades(self,course,grade):
         if course in self.grades:
             self.grades[course] = grade

     def print_grades(self):
         print(f"学生：{self.name}（学号：{self.num}）的成绩为：")
         for course in self.grades:
             print(f"{course}: {self.grades[course]} 分")


zhuolin = Studnet("卓雨",1005)
zhuolin.set_grades("语文",94)
zhuolin.set_grades("数学",95)
zhuolin.set_grades("英语",90)
zhuolin.print_grades()

# print(zhuolin.grades)