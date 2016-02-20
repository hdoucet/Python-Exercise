#!/use/bin/env python
import os

os.system('clear')

name = raw_input('Please provide you name: ')
age = int(raw_input('Please provide your age: '))
times = int(raw_input('How many time would you like the answer be printed :'))
year = 2016
hunderd = year - age + 100

for item in range(times):
	print "\n\nHello, {naam} you will turn 100 in {jaartal}.\n\n".format (naam = name, jaartal = hunderd)

