"""
Blacklist Name Matcher
Command line program
description: takes in 1-2 files (absolute file path or filename if correct location) and a query. 
    One file contains terrorist names (one in every name, no special encoding)
    The other (optional) contains noise text (words that are irrelevant, but might exist in the first file)
    The query is first strict matched against terrorist names
        e.g. Osama Bin Laden = OSAMA bin LADEN != Bin Laden, Osama != Osama Laden
    Then, if no strict match, modified (partial) match search is performed and relative certainty also presented
    	e.g. Osama Bin Laden = OSAMA bin LADEN (strict match - no partial match search performed)
    	e.g. Obama Bin Laden ~ OSAMA bin LADEN ~ Bin Laden, Osama ~ Osama Laden (no strict match, partial search results)
readme: see readme.md
license: see license.txt
"""

import terrorist_finder as terrorist_finder

query = raw_input("Please enter name to search in the terrorist list \n> ")

source_choice = raw_input("Do you want to import a file or use the EUROPA database? (Input 'file', otherwise EUROPA is used) \n> ")

if source_choice.upper() == "FILE":
	blacklist = raw_input("Please enter name of blacklist file in same path (e.g. blacklist.tsv) or absolute location \n> ")

	noisefile = raw_input("Please enter name of noise file in same path (e.g. noisefile.tsv) or absolute location \n> ")

	terrorist_finder.terrorist_finder(query, "file", blacklist, noisefile)

else:
	import scraper as scraper
	print "We will use the default sanctions list on ec.europa.eu and 8110 records (as at 27.12.2016)"
	print ""
	print "Give it a few seconds..."
	print ""
	blacklist = scraper.scraper(8110, 'http://ec.europa.eu/external_relations/cfsp/sanctions/list/version4/global/global.xml')
	noisefile = []

	terrorist_finder.terrorist_finder(query, "europa", blacklist, noisefile)