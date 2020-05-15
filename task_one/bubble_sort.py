class BubbleSort:
    name = "小花"
    list1 = [11, 9, 8, 10, 4, 50, 28]

    # 分别使用关键字参数，以及默认参数的方式传参
    def func(self):
        print("我没有传入参数")

    def func1(self, name):
        print("我有传入参数，名字叫" + name)
        return name

    def bubble_sort(self, list1):

        # 排序次数
        for i in range(1, len(list1)):
            print("这是第{}次排序".format(i))
            # 对比次数
            for j in range(len(list1) - i):

                print("这是第{}对比".format(j))

                # 如果前面一位数大于后一位数，进行位置调换
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]


bs = BubbleSort()
# 函数中有return和没有return的区别
print("我没有return返回值为", bs.func())
print("我有return返回值为", bs.func1("小花"))

# 调用排序方法输出结果
bs.bubble_sort(bs.list1)
print(bs.list1)
