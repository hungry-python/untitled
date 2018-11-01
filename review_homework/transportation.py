"""
定义一个名为Vehicles 交通工具 的基类 该类中应包含str类型的成员属性brand 商标 和 color 颜色 还应包含对象方法run 行驶 在
控制台显示“我已经开动了” 和show_info 显示信息 在控制台显示商标和颜色 并编写构造方法初始化其成员属性。 编写Car 小汽车
类继承于Vehicles类 增加int型成员属性seats 座位 还应增加成员方法show_car 在控制台显示小汽车的信息 并编写构造方法。
编写Truck 卡车 类继承于Vehicles类 增加float型成员属性load 载重 还应增加成员方法show_truck 在控制台显示卡车的信息
并编写构造方法
"""
class Vehicles:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def run(self):
        print("我已经开动了")
    def show_info(self):
        print("商标：",self.brand)
        print("颜色:",self.color)
class Car(Vehicles):
    def __init__(self,seats,brand,color):
        super(Car, self).__init__(brand,color)
        self.seats=seats
    def show_car(self):
        self.show_info()
class Truck(Vehicles):
    def __init__(self,load,brand,color):
        super(Truck, self).__init__(brand, color)
        self.load=float(load)
    def show_truck(self):
        self.show_info()

if __name__ == '__main__':
    小汽车=Car(4,"BMW","红色")
    小汽车.show_car()
    卡车=Truck(10.75,"沃尔沃","银色")
    卡车.run()
    卡车.show_truck()