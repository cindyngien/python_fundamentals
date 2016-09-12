def draw_stars(lst):
	for i in xrange(len(lst)):
		if isinstance(lst[i], int):
		 print lst[i] * "@"
		elif isinstance(lst[i], basestring):
		 lst[i] = lst[i].lower()
		 print lst[i][0]*len(lst[i]) 

draw_stars([4, "Tom", 3, "Michael" ,2 , "Wendy",5])
