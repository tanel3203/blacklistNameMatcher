###################################################
# Input: raw imported file
# Output: list type processed data
# Purpose: Process raw data to a manageable form
# Methods (1):
# 		processFile(1 argument type textfile)
#			expected: one row contains one value
###################################################

import importer as importer

# File processor
def processFile(filename):
	# Get file contents
	importedFile = importer.importFile(filename)




	# Add data to list
	# \n - newline
	processedList = importedFile.split("\n")

	return processedList


print ""
print "File processed!"
print ""