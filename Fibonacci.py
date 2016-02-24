__author__ = 'hugodoucet'
#!/use/bin/env python

number = int(raw_input("How many Fibonacci numbers would you like to get generated ?"))

a= [1,1]
def addFibNumber(a):
 	a.append(a[-1] + a[-2])
 	return a

for i in range(number):
	addFibNumber(a)
 	print a

