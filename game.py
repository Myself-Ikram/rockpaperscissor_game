import random
print("........ROCK PAPER SCISSOR.......")
print("-------------------------------")
pl_score = 0
com_score = 0
def com_choice():
	computer = random.randint(1,4)
	if(computer ==1):
		computer="r"
	elif(computer ==2):
		computer="p"
	else:
		computer="s"
	return computer





def game_logic(player,computer):
	if player=='r':
		if computer == 'p':
			return False
		if computer == 's':
			return True

	elif(player=='p'):
		if computer == 's':
			return False
		if computer == 'r':
			return True
		
	elif(player=='s'):
		if computer == 'r':
			return False
		if computer == 'P':
			return True

	elif(player==computer):
		return None
	else:
		print("player haven't enter the correct input")

def game_result():
	global pl_score
	global com_score
	print("r = rock \np = paper\ns = sccissor")
	player =input("enter ur choice: ")
	computer = com_choice()

	print("player choice is: ",player)
	print("computer choice is: ",computer)

	gameResult = game_logic(player,computer)
	print("-------------------------------")
	if(gameResult==True):
		print("player won the game")
		pl_score = pl_score +1
	elif(gameResult==False):
		print("computer won the game")
		com_score = com_score +1
	elif(gameResult ==None):
		print("match is draw")
	print("       score         ")
	print("player    |  computer   ")
	print(pl_score,"        |    ",com_score)
	print("-------------------------------")


game_result()
while(True):
	print("Enter your choice for game ")
	print("1.continue")
	print("2.Exit ")

	choice = int(input())
	if(choice ==1):
		game_result()
	else:
			break
print("thanks for playing")	
