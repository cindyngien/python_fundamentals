def coinToss():
 import random
 total_heads = 0
 total_tails = 0
 for i in xrange(5):
  coin = random.randint(0, 1)
  if coin:
    total_heads += 1
    print("Attempt #" , i, "Got total heads", total_heads, "so far " "and total tails ", total_tails, "so far")
  else:
    total_tails += 1
    print("Attempt #" , i, "Got total heads", total_heads, "so far " "and total tails ", total_tails, "so far")

coinToss()