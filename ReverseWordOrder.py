__author__ = 'hugodoucet'
#!/use/bin/env python
import os,random
os.system('clear')

zin = raw_input('Please provide me a long sentence :')

zinList = zin.split(' ')
zinList = [item for item in zinList[::-1]]

print ' '.join(zinList)



