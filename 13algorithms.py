def print_1_to_255():
	for i in xrange(1,256):
		print(i)

print_1_to_255()

def print_odds():
	for i in xrange(1,256,2):
		print(i)

print_odds()

def print_and_sum():
	my_sum = 0
	for i in xrange(256): #you can just put this if you are starting at 0; python assumes 0;
	 my_sum += i
	 print(i, my_sum)

print_and_sum()

def iterate_array(lst):
	for i in range(len(lst)):
		print(lst[i])

iterate_array([2,3,4,5,6,7])

def find_max(lst):
	my_max = lst[0]
	for i in range(len(lst)):
	 if my_max < i: my_max = i
        print my_max
print("*" * 50)
find_max([-2,1,3,4,5])

def square(lst):
	for i in xrange(len(lst)):
		lst[i] = lst[i] * lst[i]
		print lst
print("*" * 50)
square([1,2,3,4])

