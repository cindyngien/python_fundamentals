import random
import string
# don't worry too much about what these two functions are doing, but feel free to discuss them with your team - but you won't be asked to implement anything like them for a while!
def randomString(val):
    letters = string.letters
    return "".join(random.choice(letters) for i in range(val))
def makeRandom():
    return [random.randint(5,45) if random.randint(0,1) else randomString(random.randint(2,7)) for y in range(10) ]

print makeRandom()

my_list = makeRandom()

print my_list
for i in xrange(len(my_list)):
    if isinstance(my_list[i], int):
		print my_list[i] * "@"
    elif my_list[i][0].islower():
		print my_list[i][::-1]
    elif my_list[i][0].isupper():
		print (my_list [i][0], len(my_list[i]))

