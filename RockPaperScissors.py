__author__ = 'hugodoucet'
#!/use/bin/env python
import os
os.system('clear')



def question(playerNames):
	playerSelect = []
	for i in [0,1]:
		print ("\n\n Hello {}, please choose between : 1)Rocks, 2)Scissors, 3)Paper.").format(playerNames[i])
		playerSelect.append(raw_input('? 1/2/3 :'))
	return playerSelect

playerNames = [raw_input('\nWhat is your name ?') for a in range(2)]

answers = question(playerNames)

while answers[0] == answers[1]:
	print "\n You have answered identical numbers, please replay.\n"
	answers = question(playerNames)

if  ((int(answers[0]) == 3) & (int(answers[1]) == 1)) | ((int(answers[0]) == 1) & (int(answers[1]) == 2)) | ((int(answers[0]) == 2) & (int(answers[1]) == 3)) :
		winner = playerNames[0]
else: 
	winner = playerNames[1]

print "The winner is {}".format(winner)



