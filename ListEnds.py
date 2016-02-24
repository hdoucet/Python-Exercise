__author__ = 'hugodoucet'
#!/use/bin/env python

a = [5, 10, 15, 20, 25]

def ListEnds(a):
	b = [a[x] for x in [0,-1]]
	return b

b = ListEnds(a)

print b	