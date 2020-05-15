#  定义一本书类
class Book:
    # 定义变量、属性
    page = 100
    name = "python的修炼"

    # rectangle = "我是长方形"
    # 定义打开的方法
    def open(self, page):
        print("请打开第{}页".format(page))

    # 定义关上的方法
    def close(self):
        print("请关上书本休息一会儿吧！！！")

    # 定义阅读的方法
    def read(self, name):
        print("我在看{}".format(name))


# 实例化类
bk = Book()
# 调用类中的属性、方法
bk.open(bk.page)
bk.close()
bk.read(bk.name)
