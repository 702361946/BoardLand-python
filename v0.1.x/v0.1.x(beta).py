# @2024
# 702361946@qq.com
# 2024.06.28立项
# python 3.12

import random
import sys

# user and time
try:
    with open("user.txt", "r+", encoding="UTF-8") as open_user:
        for txt in open_user.readlines():
            user_temp = txt.split(';')
            time = int(user_temp[3])
            user = user_temp[1]
except FileNotFoundError:
    print("错误：user文件未找到。")
    user = "user"
    time = '?'
except ValueError:
    print("错误：user文件格式不正确。")
    user = "user"
    time = '?'
except Exception as e:
    print(f"读取user文件时发生错误：{e}")
    user = "user"
    time = '?'

# 结果(输赢啥的)
try:
    with open("result.txt", "r+", encoding="UTF-8") as open_result:
        result_temp = open_result.readlines()
        if result_temp:
            result_temp = result_temp[0].strip()
            result = '?'
        else:
            result_temp = '?'
            result = '?'
except FileNotFoundError:
    print("错误：result文件未找到。")
    result = '?'
except Exception as e:
    print(f"读取result文件时发生错误：{e}")
    result = '?'


# 玩家
class Player(object):
    def __init__(self, hp, defense, attack, treatment, plate):  # hp=生命,Defense=防御,Attack=攻击,treatment=治疗
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.treatment = treatment
        self.plate = plate


# 定义玩家和怪物
player = Player(40, 0, 0, 0, 0)
monster = Player(random.randint(20, 50), 0, 0, 0, None)


# 重置玩家与怪物意图
def def_player_time():
    player.attack = 0
    player.defense = 0

    if random.randint(0, 2) == 0:
        monster.attack = random.randint(5, 10)
        monster.defense = 0
        monster.treatment = 0
    elif random.randint(0, 1) == 0:
        monster.attack = 0
        monster.defense = random.randint(3, 10)
        monster.treatment = 0
    else:
        monster.attack = 0
        monster.defense = 0
        monster.treatment = random.randint(2, 5)


# 板块
class Plate(object):
    def __init__(self, kind, grade=0, xp=0):
        self.kind = kind  # 类型 attack=攻击=0 defense=防御=1 treatment=治疗=2
        self.grade = grade  # 等级
        self.xp = xp  # 经验


# 赋值板块0-9
if True:
    temp_a = 0
    temp_b = 1
    plate0 = Plate(temp_a)
    plate1 = Plate(temp_b)
    plate2 = Plate(temp_a)
    plate3 = Plate(temp_b)
    plate4 = Plate(temp_a)
    plate5 = Plate(temp_b)
    plate6 = Plate(temp_a)
    plate7 = Plate(temp_b)
    plate8 = Plate(temp_a)
    plate9 = Plate(temp_b)
    plate_list = [plate0, plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8, plate9]
    plate_kind_list = ['攻击', '防御', '治疗']


# 骰子
class Dice(object):
    def __init__(self, use):  # point=点数 _min随机最小值 _max随机最大值 use使用0未使用1使用
        min_t = random.randint(1, 5)
        max_t = random.randint(min_t + 1, 6)
        self.point = random.randint(min_t, max_t)
        self.point_min = min_t
        self.point_max = max_t
        self.use = use


# 赋值骰子
if True:
    dice0 = Dice(1)
    dice1 = Dice(1)
    dice2 = Dice(1)
    dice3 = Dice(1)
    dice4 = Dice(1)
    dice_list = [dice0, dice1, dice2, dice3, dice4]


# 重赋值骰子函数
def def_dice(dice, point_t_min, point_t_max):  # _t指骰子 _min指骰子最小值 _max指骰子最大值
    dice.point = random.randint(point_t_min, point_t_max)
    dice.use = 0


# 重制全部骰子
def def_dice_100():
    def_dice(dice0, dice0.point_min, dice0.point_max)
    def_dice(dice1, dice1.point_min, dice1.point_max)
    def_dice(dice2, dice2.point_min, dice2.point_max)
    def_dice(dice3, dice3.point_min, dice3.point_max)
    def_dice(dice4, dice4.point_min, dice4.point_max)


# 使用骰子
def def_dice_use(dice, plate):
    t1 = 0
    while t1 < 1:
        input0 = input('0 使用\n1 放弃')
        if input0 == '0':
            dice.use = 1
            plate.xp += 1
            # 类型 a=attack=攻击 d=defense=防御 t=treatment=治疗
            # 没写完
            if plate.kind == 'a':
                player.attack = dice.point
            elif plate.kind == 'd':
                player.defense = dice.point
            elif plate.kind == 't':
                player.hp = player.hp + dice.point
        elif input0 == '1':
            t1 = 1
        else:
            print('请输入正确的值')
            t1 = 0


# 退出
def def_exit():
    sys.exit()


# 将配置录入txt
def def_open_user():
    try:
        with open('user.txt', 'w', encoding='UTF-8') as open_user:
            open_user.write(f"user;{user};time;{time}")
    except Exception as e:
        print(f"写入用户文件时发生错误：{e}")


# 将结果录入txt
def def_open_result(result):
    try:
        with open('result.txt', 'w', encoding='UTF-8') as open_result:
            open_result.write(str(result))
    except Exception as e:
        print(f"写入结果文件时发生错误：{e}")


def def_user():
    global user
    temp = input('如何称呼您?(输入up以复用上一次的用户名)')
    if not temp == 'up':
        user = temp
    def_open_user()
    print('欢迎:' + user)


def def_result_user_up():
    print('上一次回合数:' + str(time))
    print('上一次的用户名:' + user)
    print('上一次的结果:' + result)


def def_result(result_t):
    global result
    if result_t == '0':
        result = '输'
    elif result_t == '1':
        result = '赢'
    else:
        result = '?'


# 上一次读取
progress_player_hp = 0
progress_monster_hp = 0
progress_time = 0
progress_plate = 0


def def_read_progress():
    try:
        with open('game_progress.txt', 'r+', encoding='UTF-8') as open_progress:
            for txt in open_progress.readlines():
                open_progress_temp = txt.strip().split(';')
                # 确保分割后的列表有足够的元素来防止索引错误
                if len(open_progress_temp) >= 10:
                    global progress_plate
                    global progress_player_hp
                    global progress_monster_hp
                    global progress_time
                    progress_player_hp = int(open_progress_temp[1])
                    progress_monster_hp = int(open_progress_temp[3])
                    progress_time = int(open_progress_temp[5])
                    progress_plate = int(open_progress_temp[7])
                    progress_t = int(open_progress_temp[9])
                else:
                    raise ValueError("Progress data format is incorrect.")
    except FileNotFoundError:
        print("The file 'game_progress.txt' was not found.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# 游戏记录写入
def def_open_progress():
    try:
        with open('game_progress.txt', 'w+', encoding='UTF-8') as open_progress:  # 使用写入+读取模式
            open_progress.write(f'p_hp;{player.hp};m_hp;{monster.hp};time;{time};plate;{player.plate};temp;0')
    except IOError as e:  # IOError 用于捕获输入输出错误
        print(f"An I/O error occurred: {e}")
    except Exception as e:  # 捕获其他可能的异常
        print(f"An unexpected error occurred: {e}")


# 可用骰子提醒
def def_dice_reminder_use0():
    temp = 0

    def def_temp(dice):
        if dice.use == 0:
            print(f'骰子{temp + 1}可用,点数为{dice.point}')

    while temp < 5:
        if temp == 0:
            def_temp(dice0)
        elif temp == 1:
            def_temp(dice1)
        elif temp == 2:
            def_temp(dice2)
        elif temp == 3:
            def_temp(dice3)
        elif temp == 4:
            def_temp(dice4)

        temp += 1


# 所处板块提醒
def def_plate_reminder():
    if plate_list[player.plate].kind == 0:
        temp = plate_kind_list[0]
    elif plate_list[player.plate].kind == 1:
        temp = plate_kind_list[1]
    elif plate_list[player.plate].kind == 2:
        temp = plate_kind_list[2]

    print(f'你在板块{player.plate + 1}上,板块类型为{temp}')


# 怪物意图提醒
def def_monster_adt():
    if not monster.attack == 0:
        print(f'怪物准备对你造成{monster.attack}点伤害')
    elif not monster.defense == 0:
        print(f'怪物目前拥有{monster.defense}点防御')
    elif not monster.treatment == 0:
        print(f'怪物准备回复{monster.treatment}点生命')
    else:
        print('怪物无操作')


# 骰子使用
dice_list_use0 = []


# 可用骰子用户选择页提醒
def def_user_dice_use_0():
    tt = 0
    print('0 取消')

    while tt < len(dice_list):

        if dice_list[tt].use == 0:
            print(f'{tt + 1} 骰子{tt + 1},点数为{dice_list[tt].point}')
            dice_list_use0.append(dice_list[tt])

        else:
            dice_list_use0.append(None)

        tt += 1


# 移动
def def_user_dice_move():
    tt = 0
    while tt < 1:

        tt = 1
        temp = input('请输入')

        if temp == '0':
            tt = 1
        elif temp == '1' and dice0.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
        elif temp == '2' and dice1.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
        elif temp == '3' and dice2.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
        elif temp == '4' and dice3.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
        elif temp == '5' and dice4.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
        else:
            tt = 0
            print('请输入正确的值')

        if player.plate > 9:
            player.plate -= 10
            print(f'错误提醒,目前实际在板块{player.plate + 1}上')


# 骰子使用_板块
def def_user_dice_plate():
    tt = 0
    while tt < 1:

        tt = 1
        t = '?'
        temp = input('请输入')

        if temp == '0':
            tt = 1
        elif temp == '1' and dice0.use == 0:
            dice_list[int(temp) - 1].use = 1
            t = dice0.point
        elif temp == '2' and dice1.use == 0:
            dice_list[int(temp) - 1].use = 1
            t = dice1.point
        elif temp == '3' and dice2.use == 0:
            dice_list[int(temp) - 1].use = 1
            t = dice2.point
        elif temp == '4' and dice3.use == 0:
            dice_list[int(temp) - 1].use = 1
            t = dice3.point
        elif temp == '5' and dice4.use == 0:
            dice_list[int(temp) - 1].use = 1
            t = dice4.point
        else:
            tt = 0
            t = '?'
            print('请输入正确的值')

        if not t == '?':

            if plate_list[player.plate].kind == 0:
                player.attack += t
                print(f'预计造成{player.attack}点伤害')

            elif plate_list[player.plate].kind == 1:
                player.defense += t
                print(f'预计拥有{player.defense}点防御')

            elif plate_list[player.plate].kind == 2:
                player.treatment += t
                print(f'预计生命增加{player.defense}点')


# 补充定义
def_dice_100()
time = 1
progress_t = 1


# 信息提醒
print('如果发生错误\n请向702361946@qq.com提供错误截图')


# 欢迎页
t = 0
while t < 1:
    input0 = input('0 记录\n1 开始\n2 继续上一次的进度\n9 退出')
    if input0 == '0':
        def_result_user_up()
    elif input0 == '1':
        t = 1
        # user页调用
        def_user()
    elif input0 == '2':
        print('正在努力修复中\n(不可用')
        if int(input0) == 999999999:
            def_read_progress()
            if progress_t == 0:
                player.hp = progress_player_hp
                monster.hp = progress_monster_hp
                time = progress_time
                player.player_plate = progress_plate
                t = 1
            else:
                print('无法还原进度')
                t = 0
    elif input0 == '9':
        def_exit()
    else:
        print('请输入正确的值')

# game页
t = 0
t1 = 0
while t < 1:
    print(f'回合开始,当前回合:{time}')
    # 回合开始提醒
    # 可用骰子提醒
    def_dice_reminder_use0()
    # 所处板块提醒
    def_plate_reminder()
    # 怪物行为提醒
    def_monster_adt()
    # 用户行为阶段
    t1 = 0
    while t1 < 1:
        temp = input('0 查看可用骰子\n1 查看所在板块\n2 选择骰子并行动\n3 下一回合\n9 退出游戏')
        if temp == '0':
            def_dice_reminder_use0()

        elif temp == '1':
            def_plate_reminder()

        elif temp == '2':
            t2 = 0
            while t2 < 1:
                t2 = 1
                temp = input(f'0 移动\n1 {plate_kind_list[plate_list[player.plate].kind]}\n9 取消')

                if temp == '0':
                    def_user_dice_use_0()
                    def_user_dice_move()

                elif temp == '1':
                    def_user_dice_use_0()
                    def_user_dice_plate()

                else:
                    t2 = 0
                    print('请输入有效的值')

        elif temp == '9':
            def_exit()
            t1 = 1

        elif temp == '3':
            t1 = 1

        else:
            t1 = 0
            print('请输入有效的值')

    # 回合结束
    if True:
        t = 1
        if monster.defense >= player.attack:
            monster.defense -= player.attack
        elif monster.defense < player.attack:
            monster.hp -= player.attack

        if player.treatment > 0:
            player.hp += player.treatment

        if player.defense >= monster.attack:
            player.defense -= monster.attack
        elif player.defense < monster.attack:
            player.hp -= monster.attack

        if player.hp <= 0:
            result = 0
        elif monster.hp <= 0:
            result = 1
        else:
            t = 0
            time = time + 1
            def_player_time()
            def_dice_100()
            def_open_progress()
            print(f'\n你目前还有{player.hp}点生命')
            print(f'怪物目前还有{monster.hp}点生命\n')

# 结束页
def_open_result(result)
if result == 0:
    print('很抱歉你输了')
elif result == 1:
    print('恭喜你赢了')
input('感谢游玩\n如果发现错误请联系邮箱↓\n702361946@qq.com\n按下回车(Enter)以结束游戏')
