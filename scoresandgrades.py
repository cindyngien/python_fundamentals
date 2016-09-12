def scores_and_grades():
 for i in xrange(0, 10):
  scores = int(raw_input("Please enter a score: "))
  if scores >= 90:
	print "Score: " ,scores, "Your Grade is A"
  elif scores >=80:
	print "Score: " ,scores, "Your Grade is B"
  elif scores >= 70:
	print "Score: ", scores, "Your Grade is C"
  elif scores >= 60: 
	print "Score: ", scores, "Your Grade is D"
  else:
  	print "Please enter a value higher than 60"

scores_and_grades()

