#!/use/bin/env python
import os
os.system('clear')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(raw_input("Please provide a number :"))

# i am using a python generator to create my new list
result = [item for item in a if item < number ]

#Request number 1 - based on for loop
for item in result:
	print item

#Request number 2 - transforming generator in a list.
print list(result)

