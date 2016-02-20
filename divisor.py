__author__ = 'hugodoucet'

#!/use/bin/env python
import os

os.system('clear')

number = int(raw_input("Please provide a number :"))

output = [x for x in range(1,number+1) if number % x == 0]

print list(output)

