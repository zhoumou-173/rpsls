#coding:gbk
"""
程序目标:在Geany中新编一程序， 完成RPSLS游戏。
作者:周浩
"""
import random

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='Rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='Paper':
        return 2
    elif name=='Lizard':
        return 3
    elif name=='Scissors':
        return 4
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return 'Rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'Paper'
    elif number==3:
        return 'Lizard'
    elif number==4:
        return 'Scissors'
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    print("---------------")
    print("你的选择为:",player_choice)
    player_choice_number=name_to_number(player_choice)
    a=player_choice_number
    comp_number=random.randrange(0,4)
    b=comp_number
    comp_choice=number_to_name(comp_number)
    print("计算机的选择为:",comp_choice)
    diff=a-b
    if diff==0:
        print("您和计算机出的一样呢")
    elif (diff==-2) or (diff==-1) or (diff==3) or (diff==4):
        print("计算机赢了")
    elif (diff==-4) or (diff==-3) or (diff==1) or (diff==2):
	    print("你赢了")
    else:
        print("Error:No Correct Name")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
