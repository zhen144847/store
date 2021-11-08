class glass:
    __height = 0
    __volume = 0
    __color = ''
    __material = ''

    def set_height(self,height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_volume(self,volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_material(self,material):
        self.__material = material

    def get_material(self):
        return self.__material

    def storage_liquid(self):
        print('这个水杯是', self.__material, '做的，是', self.__color, '，有', self.__height, '公分高，能放', self.__volume, '升水')

if __name__ == '__main__':
    g = glass()

    g.set_height(20)
    g.set_color('红色')
    g.set_volume(0.5)
    g.set_material('钛合金')

    g.storage_liquid()