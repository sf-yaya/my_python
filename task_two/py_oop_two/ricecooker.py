# 定义一个电饭锅类
class RiceCooker:
    # 定义变量
    size = "4升"
    shape = "球形"

    # 定义函数、方法
    def cook_rice(self, size):
        print("我的容量很多大,{}，可以煮很多米饭".format(size))

    def stew_soup(self):
        print("我煲的汤好香呀！")


# 实例化类
rc = RiceCooker()
# 调用类的属性、方法
rc.cook_rice(rc.size)
rc.stew_soup()
print(rc.shape)
