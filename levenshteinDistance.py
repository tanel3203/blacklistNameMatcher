# Levenshtein distance calculator
def levDist(str1, str2):

	# Input lenghts
	strLen1 = len(str1)
	strLen2 = len(str2)

	# Create Levenshtein distance matrix
	d = [[0 for x in range(strLen1+1)] for y in range(strLen2+1)]

	print ""
	print "Empty matrix done:"
	for s in range(len(d)):
		print d[s]
	print ""

	# Number columns and rows
	for i in range(strLen1+1):
		d[0][i] = i

	for j in range(strLen2+1):
		d[j][0] = j

	# Fill matrix
	for i in range(1,strLen1+1):
		for j in range(1,strLen2+1):
			if str1[i-1] == str2[j-1]:
				substitionCost = 0
			else:
				substitionCost = 1
			d[j][i] = min(d[j-1][i]+1,
					d[j][i-1]+1,
					d[j-1][i-1]+substitionCost)


	print "Completed matrix done: "
	for s in range(len(d)):
		print d[s]

	# Return corner value
	return d[strLen2][strLen1]

