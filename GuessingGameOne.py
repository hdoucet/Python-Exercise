__author__ = 'hugodoucet'
#!/use/bin/env python
import os,random
os.system('clear')
username = raw_input('Tell me your name :')
times = 0
parameter = ''
i = random.randint(1,9)

while True:
	times += 1
	print i
	answer = raw_input ("\n Hello, please give me a number between 0-10 :")
	if int(answer) < i:
		parameter = "low"
		
	elif int(answer) > i:
		parameter = "high"
	else:
		print "\nYou guessed the correct number !!! in {} times".format(times)
		More = raw_input("Would you like to continue ? (Y/N)")
		if More == "Y":
			break
		else:
			print ("You did not enter Y, so we play another game.")
			i = random.randint(1,9)

	print ("\n {}, alsmost correct, you guessed to {}.".format(username,parameter))


