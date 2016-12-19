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
license: see licence.txt
"""

import terrorist_finder as terrorist_finder

query = raw_input("Please enter name to search in the terrorist list \n> ")

blacklist = raw_input("Please enter name of blacklist file in same path (e.g. blacklist.tsv) or absolute location \n> ")

noisefile = raw_input("Please enter name of noise file in same path (e.g. noisefile.tsv) or absolute location \n> ")



terrorist_finder.terrorist_finder(query, blacklist, noisefile)