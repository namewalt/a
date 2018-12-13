import random               #调用随机函数
print("========== 1.开始游戏 2.退出 =========")
j = int(input())
if j == 1:
    while j == j:
        print("========== 请输入   0剪刀 1石头 2步 ==========")
        player = int(input())
        #player = int(input(" 请输入  0剪刀,1石头,2布: "))
        if player != 0 and player != 1 and player != 2:
            player = int(input("输入有误 请重新输入:"))
        computer = random.randint(0,2)   #利用随机函数生成computer输入数据
        if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            print('========== 牛逼,赢了,牛逼啊 ==========')
        elif player == computer:
            print("========== 平局,不分秋色 =========")
        else:
            print("========== 太菜了,洗洗睡吧 ==========")
        print("========= 请选择是否继续游戏 1.继续 2.退出 ==========")
        a = int(input())
        if a == 2:
            break
print("==========GoodBye!!!==========")



