test = input("请输入一篇英语短文:\n")
i = 1
while i == 1:
    play = int(input("请输入你需要进行的操作:\n          1.查询单词出现次数\n          2.查询单词首次出现的位置\n          3.全篇字母改为大写\n          4.全篇字母小写\n          5.对文中某个单词进行替换\n          6.使单词首字母全为大写\n\n"))
    print('')
    if play == 1:
        world = input("请输入你要查询的单词:\n")
        num = test.count(world)
        print("该单词出现的次数为:%d\n"%num)
    elif play == 2:
        world = input("请输入你要查询的单词:\n")
        num = test.find(world)
        if num == -1:
            print("该单词不存在\n")
        elif num != -1:
            print("该单词首次出现的位置为:%d\n"%num)
    elif play == 3:
        num = test.upper()
        print("大写后的文章为%s\n"%num)
    elif play == 4:
        num = test.lower()
        print("小写后的文章为%s\n"%num)
    elif play == 5:
        world = input("请输入你要替换的单词:\n")
        num = test.replace(world,input("请输入替换后的单词\n"))
        print("替换后的文章内容为:%s\n"%num)
    elif play == 6:
        num = test.title()
        print("首字母大写后:%s\n"%num)
    i = int(input("是否继续查看?\n          1.继续\n          2.退出\n"))

    print('')
print("          GoodBye!!!")
