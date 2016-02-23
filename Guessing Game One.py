__author__ = 'hugodoucet'
#!/use/bin/env python
import os,random
os.system('clear')
username = raw_input('Tell me your name :')
times = 0
parameter = ''

while true:
	i = random.randint(1,9)
	times += times
	answer = raw_input ("\n Hello ",username,", please give me a number between 0-10 :")
	if answer < i:
		parameter = "low"
		
	elif answer >i:
		parameter = "high"
	else answer == i:
		print "You guessed the correct number !!! in {} times".format(times)
		break

	print ("\n {}, alsmost correct, you guessed to {}.".format(username,parameter))


