

import cleaner as clean
import levenshteinDistance as levDist


def calcLev(queryString, blacklistDataFile, noiseDataFile):
	query = queryString
	blacklist = clean.cleaner(blacklistDataFile, noiseDataFile)
	levList = []
	levDistAccuracy = []


	for name in blacklist:
		currentDist = levDist.levDist(query,name)
		print currentDist, " ", len(query), " ", len(name)
		levDistAccuracy.append(currentDist/len(query))
		levList.append(currentDist)

	print ".."
	print "levDistAccuracy: ", levDistAccuracy
	print "levList: ", levList
	print ".."
	print ""
	return levList





print ""
print calcLev("Osama Ahmed Bin Ten Laden", "blacklist.txt", "noisefile.txt")
print ""