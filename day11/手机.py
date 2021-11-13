
import time

class Old_Phone:
    __brand = ''

    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def call(self, name):
        return '正在给%s打电话' % name

class New_Brand(Old_Phone):
    def call(self, name):
        print('语音拨号中')
        for i in range(3):
            print('.', end='')
            time.sleep(1)
        print(super(New_Brand, self).call(name))

    def phone_brand(self):
        print('品牌为%s的手机很牛逼' % self.get_brand())

if __name__ == '__main__':
    new = New_Brand()

    new.set_brand('华为')
    new.phone_brand()
    new.call('好大儿')




































