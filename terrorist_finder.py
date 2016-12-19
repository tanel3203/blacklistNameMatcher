"""
Input: query string, 1-2 lists (blacklist (and noise))
Output: terrorist name and certainty level, if relevant
Purpose: Find terrorists in blacklist
Methods (3):
       strict_match(1 query string, 1 list)
       partial_match(1 query string, 1 list)
        terrorist_finder(1 query string, 
                       1-2 argument(s) type textfile)
"""

import cleaner as clean
import re

def strict_match(query, blacklist):
    for name in blacklist:
        if (name.upper() == query.upper()):
            return query
    return 

def partial_match(query,blacklist):
    edited_query = query.split()
    edited_query_len = len(edited_query)
    search_obj_len = 0

    # Initialize return objects
    match_name = []
    match_certainty = []

    # Find all partial matches for terrorists
    for terrorist in blacklist:
        for partOfName in edited_query:
            search_obj = re.search(partOfName.upper(),terrorist.upper())
            if (search_obj):
                search_obj_len += 1
        if (search_obj_len > 0):
            match_name.append(terrorist)
            match_certainty.append(round(100*(float(search_obj_len)/float(edited_query_len)),2))
            search_obj_len = 0

    return match_name, match_certainty

def terrorist_finder(query_string, blacklist_data_file, noise_data_file = []):
    query = query_string
    blacklist = clean.cleaner(blacklist_data_file, noise_data_file)

    # Strict matching
    if (strict_match(query,blacklist)):
        print "TERRORIST MATCHED!"
        print "Certainty: Strict match"
        print "Name: ", query 
        return ""
    else:
        print "No strict match, looking for partial matches..."

    # Partial matching
    matches = partial_match(query,blacklist)
    match_name = matches[0]
    match_certainty = matches[1]
    if (len(match_name) > 0):
        for index,name in enumerate(match_name):
            print "TERRORIST MATCHED!"
            print "Certainty: ", match_certainty[index], "%"
            print "Name: ", name
            print ""
        return ""
    else:
        print "No partial match"

    # Fuzzy matching
    # Not implemented yet

    return ""