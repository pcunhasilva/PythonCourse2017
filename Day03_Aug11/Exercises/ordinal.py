#Write a function that takes an integer as an input and returns a script with the ordinal number
#For example, for 1, it should give "1st"
#Write a test for your function

def myfunction(i):
	if i % 1 != 0:
		raise "This is not an integer"
	if len(str(i)) == 1:
		if i == 1:
			i = str(i)+"st"
		elif i == 2:
			i = str(i)+"nd"
		elif i == 3:
			i = str(i)+"rd"
		else:
			i = str(i)+"th"
	else:
		if str(i)[-1] == "1":
			i = str(i)+"st"
		elif str(i)[-1] == "2":
			i = str(i)+"nd"
		elif str(i)[-1] == "3":
			i = str(i)+"rd"
		else:
			i = str(i)+"th"
	return i
