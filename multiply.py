def multiply(a, m):
	for i in xrange(len(a)):
	 a[i] = a[i] * m
	return a
b = multiply([2,4,10,16,5],5)
print b