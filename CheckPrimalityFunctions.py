__author__ = 'hugodoucet'
#!/use/bin/env python
import os,random
os.system('clear')
div = []

def question(qtype,text ="Give me a "):
	print "{}{} :".format(text,qtype)
	return raw_input() 


number = int(question("letter"))

for i in range(2,number):
	if number % i != 0:
		type = ""
	else:
		type = "not"
		break

print "This number is {} a prime number".format(type)		
