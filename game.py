# @2024
# 702361946@qq.com
# 2024.06.28立项
# python 3.12

from configure import *
# 补充定义
result = def_result(result_temp)
def_dice_reset()
time = 1
progress_t = 1


# 信息提醒
print('如果发生错误\n请向702361946@qq.com提供错误截图')


# 欢迎页
t = 0
while t < 1:
    input0 = input('0 记录\n1 开始\n2 继续上一次的进度\n9 退出')
    if input0 == '0':
        def_result_up()
    elif input0 == '1':
        t = 1
        # user页调用
        def_user()
    elif input0 == '2':
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
    # 回合开始提醒
    print(f'回合开始,当前回合:{time}')
    # 药水获取
    if (time - 1) % 3 == 0:
        def_potion_get()
    # 可用骰子提醒
    def_dice_reminder_use0()
    # 所处板块提醒
    def_plate_reminder()
    # 怪物行为提醒
    def_monster_adt()
    # 用户行为阶段
    t1 = 0
    while t1 < 1:
        temp = input('0 查看可用骰子\n1 查看所在板块\n2 选择骰子并行动\n3 查看药水\n4 使用药水\n7 查看怪物意图\n8 下一回合\n9 退出游戏')
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
                    up = def_user_dice_move()

                elif temp == '1':
                    def_user_dice_use_0()
                    up = def_user_dice_plate(up)

                else:
                    t2 = 0
                    print('请输入有效的值')

        elif temp == '3':
            def_potion_check()

        elif temp == '4':
            def_potion_use()

        elif temp == '7':
            def_monster_adt()

        elif temp == '8':
            t1 = 1

        elif temp == '9':
            def_exit()

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
            def_dice_reset()
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
def_exit()
