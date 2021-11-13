class computer:
    __size = 0
    __price = 0
    __processor = 0
    __memory = 0
    __continue_time = 0

    def set_size(self,size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_processor(self,processor):
        self.__processor = processor

    def get_processor(self):
        return self.__processor

    def set_memory(self,memory):
        self.__memory = memory

    def get_memory(self):
        return self.__memory

    def set_continue_time(self,continue_time):
        self.__continue_time = continue_time

    def get_continue_time(self):
        return self.__continue_time


    def typewriting(self):
        print('typewriting~')

    def play_game(self):
        print('playing games')

    def watching(self):
        print('watching')

if __name__ == '__main__':
    a = computer()

    a.typewriting()
    a.watching()
    a.play_game()