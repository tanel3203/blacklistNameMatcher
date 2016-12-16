###################################################
# Input: list type processed data
# Output: 
# Purpose: Remove irrelevant values from main file
# Methods (1):
# 		cleaner(1-2 argument(s) type textfile)
###################################################

import processor as processor
import re

def cleaner(fileToBeCleaned, noiseFileToCleanWith = []):

	# Define contents to be cleaned
	fileShiny = processor.processFile(fileToBeCleaned)
	# Exit method if nothing to clean
	if (len(noiseFileToCleanWith) == 0): return fileShiny
	# Define noise to clean 
	fileNoisy = processor.processFile(noiseFileToCleanWith)

	# Find noise in names 
	for index, name in enumerate(fileShiny):
		for noise in fileNoisy:
			if (re.search(noise, name)):

				# Remove the noise and trim the string in file and current string 
				fileShiny[index] = name.replace(noise, "").strip()
				name = name.replace(noise, "").strip()

	return fileShiny

print ""
print "Cleaning done!"
print ""