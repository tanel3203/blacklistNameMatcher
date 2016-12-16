###################################################
# Input: None
# Output: raw imported file contents
# Purpose: Get raw data from file
# Methods (1):
# 		importFile(1 argument type textfile)
###################################################

# File import
def importFile(filename): 
	try:
		myFile = open(filename)
		myDoc = myFile.read()
	except:
		myDoc = ""

	return myDoc

print ""
print "File imported!"
print ""