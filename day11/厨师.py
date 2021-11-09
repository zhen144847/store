
class Chek:
    __name = ""
    __age = 0


    def Steam(self):
        pass

    def __set_name(self,name):
        self.__name = name
    def __get_name(self):
        return self.__name

    def __set_age(self, age):
        self.__age = age
    def __get_age(self):
        return self.__age


class Cheks(Chek):
    def fried(self):
        pass

class Chekess(Cheks):
    def Steam(self):
        print()
        print("正在蒸饭，金子做的米饭")

    def fried(self):
        print()
        print("正在炒菜，红烧肉炖大鹅")

if __name__ == '__main__':
    t = Chekess()
    t.set_age(20)
    t.set_name('张三')

    print('厨师叫%s，已经%s岁大了' % (t.get_name(), t.get_age()))

    t.Steam()
    t.fried()

















