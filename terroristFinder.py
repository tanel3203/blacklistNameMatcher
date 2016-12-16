##########################################################
# Input: query string, 1-2 lists (blacklist (and noise))
# Output: terrorist name and certainty level, if relevant
# Purpose: Find terrorists in blacklist
# Methods (3):
#		strictMatch(1 query string, 1 list)
#		partialMatch(1 query string, 1 list)
# 		terroristFinder(1 query string, 
#						1-2 argument(s) type textfile)
##########################################################

import cleaner as clean
import re

def strictMatch(query, blacklist):
	for name in blacklist:
		if (name.upper() == query.upper()):
			return query
	return 

def partialMatch(query,blacklist):

	editedQuery = query.split()
	editedQueryLen = len(editedQuery)
	searchObjLen = 0

	matchName = []
	matchCertainty = []

	for terrorist in blacklist:
		for partOfName in editedQuery:
			searchObj = re.search(partOfName.upper(),terrorist.upper())
			if (searchObj):
				searchObjLen += 1
		if (searchObjLen > 0):
			matchName.append(terrorist)
			matchCertainty.append(round(100*(float(searchObjLen)/float(editedQueryLen)),2))
			searchObjLen = 0

	return matchName, matchCertainty

def terroristFinder(queryString, blacklistDataFile, noiseDataFile = []):
	query = queryString
	blacklist = clean.cleaner(blacklistDataFile, noiseDataFile)


	# Strict matching
	if (strictMatch(query,blacklist)):
		print "TERRORIST MATCHED!"
		print "Certainty: Strict match"
		print "Name: ", query 
		return ""
	else:
		print "No strict match, looking for partial matches..."

	# Partial matching
	matches = partialMatch(query,blacklist)
	matchName = matches[0]
	matchCertainty = matches[1]
	if (len(matchName) > 0):
		for index,name in enumerate(matchName):
			print "TERRORIST MATCHED!"
			print "Certainty: ", matchCertainty[index], "%"
			print "Name: ", name
			print ""
		return ""
	else:
		print "No partial match"

	# Fuzzy matching

	return ""



#print ""
#print terroristFinder("Osama Bin Laaden", "blacklist.txt", "noisefile.txt")
#print ""



