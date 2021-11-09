import time
class person:
    name = ""
    sex = ""
    age = 0



class worker(person):
    def works(self,working):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,职业：工人，正在",working,"!!!")

class student(person):
    def studys(self,study,sing):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,是一名大学生，正在边",study,"边",sing,"!!!")

study = student()
study.name = "阿振老师"
study.sex = "仙"
study.age = 99
study.studys("学英语单词","唱日语歌")

work = worker()
work.name = "张振"
work.sex = "男"
work.age = 1000

work.works("做引体向上")























