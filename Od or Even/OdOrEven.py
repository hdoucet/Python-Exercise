#!/use/bin/env python
import os

os.system('clear')

number = int(raw_input("Please provide a number:"))


if number % 4  == 0:
	print "\n This number can be divided by 4."
elif number % 2  == 0:
	print "\n This number can be dived by 2."
else:
	print "\n This number is uneven."