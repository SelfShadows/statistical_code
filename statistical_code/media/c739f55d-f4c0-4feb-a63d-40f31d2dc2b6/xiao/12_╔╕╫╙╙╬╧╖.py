import random
class Game:
	
	def __init__(self,player1,player2):
		self.player1=player1
		self.player2=player2
		print('游戏初始化成功,可以开始')

	def start_game(self):
		self.player1.cast()
		self.player2.cast()
		print(self.player1)
		print(self.player2)
class player:
	
	def __init__(self,name,sex,*dice):
		self.name=name
		self.sex=sex
		self.dices=dice
	
	def __str__(self):
		play_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
		return '姓名为:%s,投掷骰子点数信息为:%s'%(self.name,str(play_dice_count_list))
	def cast(self):
		for dice in self.dices:
			dice.roll()

	def guess(self):
		pass

class dice:

	def __init__(self):
		self.count=0
	
	def roll(self):
		self.count=random.randint(1,6)
		
			
d1=dice()
d2=dice()
d3=dice()
d4=dice()
d5=dice()
d6=dice()

p1=player('player1','man',d1,d2,d3)
p2=player('player2','nv',d4,d5,d6)

for i in range(1,6):
	game=Game(p1,p2)
	print('第%d次游戏的情况----------'%i)
	game.start_game()
















