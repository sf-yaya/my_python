# 定义一个天山童姥类 ，类名为TongLao
class TongLao:
    # 初始化变量
    def __init__(self):
        self.ph = 1000
        self.power = 20
        self.name = ["WYZ", "李秋水", "丁春秋"]
    # 定义一个see_people类，传入参数name
    def see_people(self, name):
        # 循环name列表中的值，进行名称对比
        for i in range(len(name)):
            if name[i] == "WYZ":
                print("师弟！！！！")
            if name[i] == "李秋水":
                print("呸，贱人")
            if name[i] == "丁春秋":
                print("叛徒！我杀了你")

    # 天山折梅手方法，传入对手的血量值enemy_hp，对手的武力值enemy_power。
    def fight_zms(self, enemy_hp, enemy_power):
        # 将自己的武力值提升10倍，血量缩减2倍。
        final_hp = self.ph / 2 - enemy_power
        enemy_final_hp = enemy_hp - self.power * 10
        # 进行一回合制对打，打完之后，比较双方血
        if final_hp > enemy_final_hp:
            print("哈哈哈，我赢了")
        else:
            print("我不服，再来一局")


# 实力化类
# tl = TongLao()
# tl.fight_zms(2000,400)
# tl.see_people(tl.name)
