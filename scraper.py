"""
Input: 
Output: list type WHOLENAME
Purpose: Get europa blacklist names, process to list
Methods (1):
       scraper(int total requests, url type source xml)
NOTICE:
	It does not handle foreign keyboards (e.g. kirillitsa)
"""


import xml.etree.cElementTree as ET
import urllib2

def scraper(nodes, blacklist):
	wholenames = []

	tree = ET.ElementTree(file=urllib2.urlopen(blacklist))
	ttr = tree.findall(".//WHOLENAME")

	print "------------------------------------------------------------------------------"
	print "IMPORTANT!"
	print "If this text is followed by an error"
	print "it is most likely you requested # names that's more than there are in the list"
	print "The list has ", len(ttr), " existing names"
	print "------------------------------------------------------------------------------"

	if len(ttr) < nodes:
		raise ValueError("Content available <=", len(ttr), ", you entered: ", nodes)
	else:
		for i in range(nodes):
		    wholename = ttr[i].text
		    if len(wholename) > 0:
		    	wholenames.append(wholename)
	    
	return wholenames

