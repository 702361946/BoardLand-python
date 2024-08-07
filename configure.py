#  Copyright (c) 2024.

# @2024
# 702361946@qq.com
# 2024.06.28立项
# python 3.12

import logging
import random
import sys
# 时间
from datetime import datetime

# 日志初定义
if True:
    logging.basicConfig(filename='configure.log', filemode='w', level=logging.DEBUG, encoding='UTF-8')
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# user and time
try:
    with open("user.txt", "r+", encoding="UTF-8") as open_user:
        logging.debug('open user.txt')
        for txt in open_user.readlines():
            user_temp = txt.split(';')
            time = int(user_temp[3])
            user = user_temp[1]
except FileNotFoundError:
    print("错误：user文件未找到。")
    user = "user"
    time = '?'
    logging.error('open user.txt FileNotFoundError')
except ValueError:
    print("错误：user文件格式不正确。")
    user = "user"
    time = '?'
    logging.error('open user.txt ValueError')
except Exception as e:
    print(f"读取user文件时发生错误：{e}")
    user = "user"
    time = '?'
    logging.error(f'open user.txt error:{e}')

# 结果(输赢啥的)
try:
    with open("result.txt", "r+", encoding="UTF-8") as open_result:
        logging.debug('open result.txt')
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
    logging.error('open result.txt FileNotFoundError')
except Exception as e:
    print(f"读取result文件时发生错误：{e}")
    result = '?'
    logging.error(f'open result.txt {e}')


# 玩家
class Player(object):
    def __init__(self, hp, defense, attack, treatment, plate):  # hp=生命,Defense=防御,Attack=攻击,treatment=治疗
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.treatment = treatment
        self.plate = plate


# 定义玩家和怪物
if True:
    player = Player(40, 0, 0, 0, 0)
    logging.info('sys player ok')
    monster = Player(random.randint(20, 50), 0, 0, 0, None)
    logging.info('sys monster ok')


# 重置玩家与怪物意图
def def_player_time():
    logging.info('sys def player_time')
    # player
    if True:
        player.attack = 0
        player.defense = 0
        player.treatment = 0
        logging.info(f'sys player attack={player.attack} defense={player.defense} treatment={player.treatment}')
    # monster
    if True:
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

        logging.info(f'sys monster attack={monster.attack} defense={monster.defense} treatment={monster.treatment}')


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
    logging.info('plate ok')
    tt = 0
    while tt < len(plate_list):
        logging.debug(f'sys plate {tt} king={plate_list[tt].kind} xp={plate_list[tt].xp} grade={plate_list[tt].grade}')
        tt += 1


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
    logging.info('dice ok')
    tt = 0
    while tt < len(dice_list):
        logging.debug(f'sys dice {tt} use={dice_list[tt].use} point={dice_list[tt].point} max={dice_list[tt].point_max}'
                      f' min={dice_list[tt].point_min}')
        tt += 1


# 药水基础列表
if True:
    potion_name_list = ['移动药水', '攻击药水', '防御药水', '治疗药水', '']
    potion_user_list = []
    potion_introduction_list = ['移动至其他板块', '对怪物造成伤害', '增加自己的防御', '回复自己的血量']
    logging.info('potion_list ok')


# 药水类定义
class Potion(object):
    def __init__(self, name, p_type, value):  # value指代值 Type指代类型 0=移动 1=攻击 2=防御 3=治疗 9=无
        self.name = name
        self.type = p_type
        self.value = value


# 药水基础赋值
if True:
    potion0 = Potion(potion_name_list[-1], 9, 0)
    potion1 = Potion(potion_name_list[-1], 9, 0)
    potion2 = Potion(potion_name_list[-1], 9, 0)
    potion_user_list.append(potion0)
    potion_user_list.append(potion1)
    potion_user_list.append(potion2)
    logging.info('potion ok')
    t_list = potion_user_list
    tt = 0
    while tt < len(t_list):
        logging.debug(f'sys potion name={t_list[tt].name} type={t_list[tt].type} value={t_list[tt].value}')
        tt += 1
    del t_list


# 可用药水查看
def def_potion_check():
    temp = 0
    t = 0
    while temp < len(potion_user_list):
        if not potion_user_list[temp].type == 9:
            print(f'药水{temp + 1}:{potion_user_list[temp].name}'
                  f'可{potion_introduction_list[potion_user_list[temp].type]}'
                  f'\n点数为{potion_user_list[temp].value}')

        else:
            t += 1

        temp += 1

    if t == len(potion_user_list):
        print('无药水可用\n')

    logging.debug('user def potion_check')


# 获取药水
def def_potion_get():
    temp = 0
    t = 0
    while temp < len(potion_user_list):
        if potion_user_list[temp].type == 9:
            tt = random.randint(0, 3)
            potion_user_list[temp].type = tt
            potion_user_list[temp].name = potion_name_list[tt]
            potion_user_list[temp].value = random.randint(1, 5)
            print(f'药水添加至药水槽{temp + 1},类型为{potion_name_list[tt]},可{potion_introduction_list[tt]}')

            logging.debug(f'sys potion_get_ok name={potion_user_list[temp].name} type={potion_user_list[temp].type}'
                          f' value={potion_user_list[temp].value}')

            temp = len(potion_user_list)

        else:
            t += 1
            temp += 1

    if t == len(potion_user_list):
        print('无药水空闲槽,无法获取')

    logging.debug('user def potion_get')


# 使用药水
def def_potion_use():
    def potion_use_no_g(t_int):
        print(f'药水{t_int + 1}被使用')
        if potion_user_list[t_int].type == 0:
            player.plate += potion_user_list[t_int].value
            def_plate_reminder()

            logging.info(f'user potion plate+:{potion_user_list[t_int].value}')

        elif potion_user_list[t_int].type == 1:
            player.attack += potion_user_list[t_int].value
            print(f'预计目前可造成伤害{player.attack}')

            logging.info(f'user potion attack+:{potion_user_list[t_int].value}')

        elif potion_user_list[t_int].type == 2:
            player.defense += potion_user_list[t_int].value
            print(f'目前可防御{player.defense}点伤害')

            logging.info(f'user potion defense+:{potion_user_list[t_int].value}')

        elif potion_user_list[t_int].type == 3:
            player.treatment += potion_user_list[t_int].value
            print(f'预计可回复{player.treatment}点血量')

            logging.info(f'user potion treatment+:{potion_user_list[t_int].value}')

        potion_user_list[t_int].type = 9

    def_potion_check()
    temp = input('输入要使用的药水编号')
    if temp == '1' and not potion_user_list[int(temp) - 1].type == 9:
        potion_use_no_g(int(temp) - 1)
    elif temp == '2' and not potion_user_list[int(temp) - 1].type == 9:
        potion_use_no_g(int(temp) - 1)
    elif temp == '3' and not potion_user_list[int(temp) - 1].type == 9:
        potion_use_no_g(int(temp) - 1)
    else:
        input('不可用\n按下Enter(回车)继续')

    logging.info('user def potion_use')


# 重赋值骰子函数
def def_dice_use_true(dice, point_t_min, point_t_max):  # _t指骰子 _min指骰子最小值 _max指骰子最大值
    dice.point = random.randint(point_t_min, point_t_max)
    dice.use = 0

    logging.debug('sys def dice_use_true')


# 重置全部骰子
def def_dice_reset():
    def_dice_use_true(dice0, dice0.point_min, dice0.point_max)
    def_dice_use_true(dice1, dice1.point_min, dice1.point_max)
    def_dice_use_true(dice2, dice2.point_min, dice2.point_max)
    def_dice_use_true(dice3, dice3.point_min, dice3.point_max)
    def_dice_use_true(dice4, dice4.point_min, dice4.point_max)

    logging.debug('sys def dice_reset')


# 退出
def def_exit():
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.debug('sys exit')
    sys.exit()


# 将配置录入txt
def def_open_user():
    try:
        logging.debug('sys w user.txt')
        with open('user.txt', 'w', encoding='UTF-8') as open_user:
            open_user.write(f"user;{user};time;{time}")
    except Exception as e:
        print(f"写入用户文件时发生错误：{e}")
        logging.error(f'sys w user.txt error:{e}')


# 将结果录入txt
def def_open_result(result):
    try:
        logging.debug('sys w result.txt')
        with open('result.txt', 'w', encoding='UTF-8') as open_result:
            open_result.write(str(result))
    except Exception as e:
        print(f"写入结果文件时发生错误：{e}")
        logging.error(f'sys w result.txt error:{e}')


# user页
def def_user():
    global user
    temp = input('如何称呼您?(输入up以复用上一次的用户名)')
    if not temp == 'up':
        user = temp
    def_open_user()
    print('欢迎:' + user)
    logging.info(f'user def user is {user}')


# 上一次结果展示
def def_result_up():
    logging.info('user def result_up')
    print('上一次回合数:' + str(time))
    print('上一次的用户名:' + user)
    print('上一次的结果:' + result)


# 结果展示
def def_result(result):
    if result == '0':
        result = '输'
    elif result == '1':
        result = '赢'
    else:
        result = '?'

    logging.info('sys def result')

    return result


# # 上一次读取
# progress_player_hp = 0
# progress_monster_hp = 0
# progress_time = 0
# progress_plate = 0
#
#
# def def_read_progress():
#     try:
#         with open('game_progress.txt', 'r+', encoding='UTF-8') as open_progress:
#             for txt in open_progress.readlines():
#                 open_progress_temp = txt.strip().split(';')
#                 # 确保分割后的列表有足够的元素来防止索引错误
#                 if len(open_progress_temp) >= 10:
#                     global progress_plate
#                     global progress_player_hp
#                     global progress_monster_hp
#                     global progress_time
#                     progress_player_hp = int(open_progress_temp[1])
#                     progress_monster_hp = int(open_progress_temp[3])
#                     progress_time = int(open_progress_temp[5])
#                     progress_plate = int(open_progress_temp[7])
#                     progress_t = int(open_progress_temp[9])
#                 else:
#                     raise ValueError("Progress data format is incorrect.")
#     except FileNotFoundError:
#         print("The file 'game_progress.txt' was not found.")
#     except ValueError as ve:
#         print(f"Value error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# 游戏记录写入
# def def_open_progress():
#     try:
#         logging.debug('sys w game_progress.txt')
#         with open('game_progress.txt', 'w+', encoding='UTF-8') as open_progress:  # 使用写入+读取模式
#             open_progress.write(f'p_hp;{player.hp};m_hp;{monster.hp};time;{time};plate;{player.plate};temp;0')
#     except IOError as e:  # IOError 用于捕获输入输出错误
#         print(f"An I/O error occurred: {e}")
#     except Exception as e:  # 捕获其他可能的异常
#         print(f"An unexpected error occurred: {e}")


# 可用骰子提醒
def def_dice_reminder_use0():
    logging.info('sys or user  def doce_reminder_T')
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
    logging.info('sys or user  def plate_reminder')
    if plate_list[player.plate].kind == 0:
        temp = plate_kind_list[0]
    elif plate_list[player.plate].kind == 1:
        temp = plate_kind_list[1]
    elif plate_list[player.plate].kind == 2:
        temp = plate_kind_list[2]

    print(f'你在板块{player.plate + 1}上,板块类型为{temp}')


# 怪物意图提醒
def def_monster_adt():
    logging.info('sys or user  def monster_adt')
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
    logging.info('sys user dice use True')
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
    logging.debug('user dice_move')
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
            up = None
        elif temp == '2' and dice1.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
            up = None
        elif temp == '3' and dice2.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
            up = None
        elif temp == '4' and dice3.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
            up = None
        elif temp == '5' and dice4.use == 0:
            player.plate += dice_list[int(temp) - 1].point
            print(f'目前在板块{player.plate + 1}上')
            dice_list[int(temp) - 1].use = 1
            up = None
        else:
            tt = 0
            print('请输入正确的值')

        if player.plate > 9:
            player.plate -= 10
            print(f'错误提醒,目前实际在板块{player.plate + 1}上')

    return up


# 骰子使用_板块
up = None


def def_user_dice_plate(up):
    logging.debug('user dice_plate')
    tt = 0

    while tt < 1:

        tt = 1
        temp = input('请输入')

        def def_user_dice_plate_up():
            nonlocal t
            if up is not None:
                if up == dice_list[int(temp) - 1].point - 1:
                    t = dice_list[int(temp) - 1].point
                else:
                    print(f'骰子点数不合规\n您或许应该出点数为{str(up + 1)}的骰子以连续行动')
                    t = 'no'
            else:
                t = dice_list[int(temp) - 1].point
            return t

        if temp == '0':
            tt = 1
        elif temp == '1' and dice0.use == 0:
            t = def_user_dice_plate_up()
            if not t == 'no':
                dice_list[int(temp) - 1].use = 1
                plate_list[player.plate].xp += 1

        elif temp == '2' and dice1.use == 0:
            t = def_user_dice_plate_up()
            if not t == 'no':
                dice_list[int(temp) - 1].use = 1
                plate_list[player.plate].xp += 1

        elif temp == '3' and dice2.use == 0:
            t = def_user_dice_plate_up()
            if not t == 'no':
                dice_list[int(temp) - 1].use = 1
                plate_list[player.plate].xp += 1

        elif temp == '4' and dice3.use == 0:
            t = def_user_dice_plate_up()
            if not t == 'no':
                dice_list[int(temp) - 1].use = 1
                plate_list[player.plate].xp += 1

        elif temp == '5' and dice4.use == 0:
            t = def_user_dice_plate_up()
            if not t == 'no':
                dice_list[int(temp) - 1].use = 1
                plate_list[player.plate].xp += 1

        else:
            tt = 0
            t = '?'
            print('请输入正确的值')

        if not t == '?' and t is not None and not t == 'no':

            if plate_list[player.plate].kind == 0:
                player.attack += t
                if plate_list[player.plate].grade > 0:
                    player.attack += plate_list[player.plate].grade * 2
                print(f'预计造成{player.attack}点伤害')

            elif plate_list[player.plate].kind == 1:
                player.defense += t
                if plate_list[player.plate].grade > 0:
                    player.defense += plate_list[player.plate].grade
                print(f'预计拥有{player.defense}点防御')

            elif plate_list[player.plate].kind == 2:
                if plate_list[player.plate].grade > 0:
                    if plate_list[player.plate].grade == 1 and t > 4:
                        t = 4
                    elif plate_list[player.plate].grade == 2 and t > 5:
                        t = 5
                player.treatment += t
                print(f'预计生命增加{player.treatment}点')

    if True:
        def_plate_up()
        return t


# 板块等级与经验查看
def def_plate_xpg():
    logging.info('user def plate_xgg')
    print(f'目前在板块{player.plate + 1}上\n板块经验为{plate_list[player.plate].xp}\n板块等级为{plate_list[player.plate].grade}')
    input('按下Enter(回车)继续')


# 板块升级
def def_plate_up():
    logging.debug('sys def plate_up')

    def def_plate_up_t(t0_int):
        print('板块升级')
        tt = 0
        up_0 = random.randint(0, 2)
        up_1 = random.randint(0, 2)
        while up_1 == up_0:
            up_1 = random.randint(0, 2)
        if t0_int == 0:
            while tt < 1:
                tt = 1
                temp = input(f'0 {plate_kind_list[up_0]}\n1 {plate_kind_list[up_1]}')
                if temp == '0':
                    plate_list[player.plate].kind = up_0
                    print(f'板块类型已改为{plate_kind_list[up_0]}')
                    plate_list[player.plate].grade += 1
                elif temp == '1':
                    plate_list[player.plate].kind = up_1
                    print(f'板块类型已改为{plate_kind_list[up_1]}')
                    plate_list[player.plate].grade += 1
                else:
                    tt = 0
                    print('请输入正确的值')
        elif t0_int == 1:
            while tt < 1:
                tt = 1
                temp = input(f'0 升级\n1 更改类型为{plate_kind_list[up_0]}')
                if temp == '0':
                    plate_list[player.plate].grade += 1
                elif temp == '1':
                    plate_list[player.plate].kind = up_0
                    print(f'板块类型已改为{plate_kind_list[up_0]}')
                else:
                    tt = 0
                    print('请输入正确的值')

    if plate_list[player.plate].xp >= 3 and plate_list[player.plate].grade == 0:
        def_plate_up_t(0)
    elif plate_list[player.plate].xp >= 8 and plate_list[player.plate].grade == 1:
        def_plate_up_t(1)
    elif plate_list[player.plate].xp >= 15 and plate_list[player.plate].grade == 2:
        def_plate_up_t(1)
