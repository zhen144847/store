


from threading import Thread
from queue import Queue
import time

q = Queue()
lanzi = 0
in_count = 0
sell_count = 0


class chushi(Thread):
    num = 0

    def run(self) -> None:
        while True:
            global lanzi
            lanzi = lanzi+3
            start = time.perf_counter()
            if lanzi == 500:
                print("篮子满了")
                time.sleep(3)
            if lanzi < 500:
                print("篮子里还有%s个蛋挞"%lanzi)
                lanzi += 3
            else:
                salary = sell_count * 2.5
                print('厨师的工资为%s元' % salary)

class shouyin(Thread):
    def run(self):
        global in_count
        global lanzi
        global sell_count
        start = time.perf_counter()
        while True :
            end = time.perf_counter()
            if end - start > 180:
                break
            else:
                print('卖了%s个蛋挞，共计收入%s元' % (sell_count, in_count))

class guke(Thread):
    __name = ''
    count = 0
    user_money = 5000
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self) -> None:
        global lanzi, sell_count, in_count


        start = time.perf_counter()
        while self.user_money > 3:
            if lanzi == 0:
                print('篮子空了，%s停4秒' % self.get_name())
                time.sleep(4)
            else:
                in_count += 3
                sell_count += 1
                lanzi -= 1
                self.count += 1
                self.user_money -= 3
                end = time.perf_counter()
                if end - start > 180:
                    break
            print('%s抢了%s个蛋挞，还剩%s元' % (self.get_name(), self.count, self.user_money))

t1 = chushi()
t2 = shouyin()
t3 = guke()
t4 = guke()
t5 = guke()
t6 = guke()

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














































































