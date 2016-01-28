#firstnum = input("Put in first number")
#secondnum = input("Put in second number")
sumnum = 0
def super_sum(*args):
    #super_sum = (sum(numbers))
	#return x +y
	total = 0
	#c = []
	print("Got arguments: ", args)
	for i in args:
		print("In for loop: total: {}, i: {}".format(total, i))
		if isinstance(i, list):
			print("Got a list: ", i)
			for a in i:
				print "Adding {} to total...".format(a)
				total += a
				print "Total is now {}.".format(total)
		else:
			total += i
		#total = sum(args)

 	return total

print(super_sum([20, 40], 10))