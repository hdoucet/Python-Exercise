#!/use/bin/env python
import os

os.system('clear')

number = int(raw_input("Please provide a number:"))
check = int(raw_input("Please provide a quotient:"))

if number % check  == 0:
	sol = ""
else:
	sol = " not"

print "\n This {number} can{sol} be divided by {quotient}.".format(number = number, sol = sol, quotient = check)

