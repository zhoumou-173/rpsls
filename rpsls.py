#coding:gbk
"""
����Ŀ��:��Geany���±�һ���� ���RPSLS��Ϸ��
����:�ܺ�
"""
import random

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
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
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
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
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("---------------")
    print("���ѡ��Ϊ:",player_choice)
    player_choice_number=name_to_number(player_choice)
    a=player_choice_number
    comp_number=random.randrange(0,4)
    b=comp_number
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ:",comp_choice)
    diff=a-b
    if diff==0:
        print("���ͼ��������һ����")
    elif (diff==-2) or (diff==-1) or (diff==3) or (diff==4):
        print("�����Ӯ��")
    elif (diff==-4) or (diff==-3) or (diff==1) or (diff==2):
	    print("��Ӯ��")
    else:
        print("Error:No Correct Name")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
