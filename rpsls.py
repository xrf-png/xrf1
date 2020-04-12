#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock。
剪刀能剪纸和蜥蜴；纸可以包住石头，驳斥Spock；石头击烂蜥蜴和剪刀；
蜥蜴可以毒害史波克，吃纸；史波克可以砸碎剪刀，使石头蒸发。
作者：肖瑞峰
日期：2020.4.12

"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):     
    if name == '石头' :
        player_choice_number=0
    if name == '史波克' :
        player_choice_number=1
    if name == '纸' :
        player_choice_number=2
    if name == '蜥蜴' :
        player_choice_number=3        
    if name == '剪刀' :
        player_choice_number=4
    return player_choice_number                                                
    """
    将游戏对象对应到不同的整数
    """
    
def number_to_name(number):   
    if number==0:
        comp_choice='石头'
    if number==1:
        comp_choice='史波克'    
    if number==2:
        comp_choice='纸'            
    if number==3:
        comp_choice='蜥蜴'            
    if number==4:
        comp_choice='剪刀'
    return comp_choice
    """
    将整数 (0, 1, 2, 3, 4)对应到游戏的不同对象
    """


def rpsls(player_choice_number,comp_number):        
    if player_choice_number == 0 and (comp_number == 3 or comp_number == 4):
        result='您赢了！'
    elif player_choice_number == 1 and (comp_number == 0 or comp_number == 4):
        result='您赢了！'
    elif player_choice_number == 2 and (comp_number == 0 or comp_number == 1):
        result='您赢了！'
    elif player_choice_number == 3 and (comp_number == 1 or comp_number == 2):
        result='您赢了！'    
    elif player_choice_number == 4 and (comp_number == 2 or comp_number == 3):
        result='您赢了！'                
    elif player_choice_number == comp_number:
        result='您和计算机出的一样呢！'
    else:
        result='机器赢了'
    return result
      
player_choice= input('请输入您的选择:')             
comp_number=random.randint(0,4)
if player_choice == '剪刀' or player_choice == '石头' or player_choice == '纸' or player_choice == '蜥蜴' or player_choice == '史波克':
	player_choice_number=name_to_number(player_choice)
	print("--------")
	print('您的选择为:'+player_choice)
	print('计算机的选择为:'+number_to_name(comp_number))
	print(rpsls(player_choice_number,comp_number))
else:
	print('Error: No Correct Name')
	
