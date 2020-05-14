"""
python实战练习2
课后作业2
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""


# 定义一个汽车类
class Car:
    # 定义变量
    wheel = 4
    steering_wheel = "我是方向盘，可以随意调整方向哦"
    horn = "我是一个小喇叭，可以发出嘀嘀嘀的声音！"

    # 定义run的方法
    def run(self, wheel):
        print("我有{}个轮子，我跑的很快哦！".format(wheel))

    # 定义一个方向的方法
    def direction(self, horn):
        print("{}".format(horn))


# 实例化类
c = Car()
# 调用类中的方法、属性
c.run(c.wheel)
c.direction(c.horn)




