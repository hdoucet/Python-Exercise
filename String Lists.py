__author__ = 'hugodoucet'
#!/use/bin/env python
import os
os.system('clear')
word = raw_input("Please provide me with a word, i'll check if it is a palindrome-type word : ")

if word == word[::-1]:
	value = " "
else:
	value = "not "

print "##{}## spelled backward is ##{}##, so it is {}a palindrome".format(word,word[::-1],value)




		