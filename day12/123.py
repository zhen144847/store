import time
from threading import Thread

egg_tart = 0
in_count = 0
sell_count = 0


class chef(Thread):
    def run(self):
        global egg_tart
        start = time.perf_counter()
        while True:

            if egg_tart == 500:
                print('篮子满了')
                time.sleep(3)
            if egg_tart < 500:
                print('篮子里有%s个蛋挞' % egg_tart)
                egg_tart += 3
            else:
                salary = sell_count * 2.5
                print('厨师的工资为%s元' % salary)


class cashier(Thread):
    def run(self):
        global in_count
        global egg_tart
        global sell_count
        start = time.perf_counter()
        while True :
            end = time.perf_counter()
            if end - start > 180:
                break
            else:
                print('卖了%s个蛋挞，共计收入%s元' % (sell_count, in_count))

class user(Thread):
    __name = ''
    count = 0
    user_money = 5000
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self) -> None:
        global egg_tart, sell_count, in_count


        start = time.perf_counter()
        while self.user_money > 3:
            if egg_tart == 0:
                print('篮子空了，%s停4秒' % self.get_name())
                time.sleep(4)
            else:
                in_count += 3
                sell_count += 1
                egg_tart -= 1
                self.count += 1
                self.user_money -= 3
            end = time.perf_counter()
            if end - start > 180:
                pass

        print('%s抢了%s个蛋挞，还剩%s元' % (self.get_name(), self.count, self.user_money))



t1 = chef()
t2 = cashier()
t3 = user()
t4 = user()
t5 = user()
t6 = user()

t3.set_name('赵六')
t4.set_name('王五')
t5.set_name('李四')
t6.set_name('张三')

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
