#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock��
�����ܼ�ֽ�����棻ֽ���԰�סʯͷ������Spock��ʯͷ��������ͼ�����
������Զ���ʷ���ˣ���ֽ��ʷ���˿������������ʹʯͷ������
���ߣ�Ф���
���ڣ�2020.4.12

"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):     
    if name == 'ʯͷ' :
        player_choice_number=0
    if name == 'ʷ����' :
        player_choice_number=1
    if name == 'ֽ' :
        player_choice_number=2
    if name == '����' :
        player_choice_number=3        
    if name == '����' :
        player_choice_number=4
    return player_choice_number                                                
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    
def number_to_name(number):   
    if number==0:
        comp_choice='ʯͷ'
    if number==1:
        comp_choice='ʷ����'    
    if number==2:
        comp_choice='ֽ'            
    if number==3:
        comp_choice='����'            
    if number==4:
        comp_choice='����'
    return comp_choice
    """
    ������ (0, 1, 2, 3, 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """


def rpsls(player_choice_number,comp_number):        
    if player_choice_number == 0 and (comp_number == 3 or comp_number == 4):
        result='��Ӯ�ˣ�'
    elif player_choice_number == 1 and (comp_number == 0 or comp_number == 4):
        result='��Ӯ�ˣ�'
    elif player_choice_number == 2 and (comp_number == 0 or comp_number == 1):
        result='��Ӯ�ˣ�'
    elif player_choice_number == 3 and (comp_number == 1 or comp_number == 2):
        result='��Ӯ�ˣ�'    
    elif player_choice_number == 4 and (comp_number == 2 or comp_number == 3):
        result='��Ӯ�ˣ�'                
    elif player_choice_number == comp_number:
        result='���ͼ��������һ���أ�'
    else:
        result='����Ӯ��'
    return result
      
player_choice= input('����������ѡ��:')             
comp_number=random.randint(0,4)
if player_choice == '����' or player_choice == 'ʯͷ' or player_choice == 'ֽ' or player_choice == '����' or player_choice == 'ʷ����':
	player_choice_number=name_to_number(player_choice)
	print("--------")
	print('����ѡ��Ϊ:'+player_choice)
	print('�������ѡ��Ϊ:'+number_to_name(comp_number))
	print(rpsls(player_choice_number,comp_number))
else:
	print('Error: No Correct Name')
	
