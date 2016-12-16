# Blacklist calculator

# Description:
* Imports a file with a list of blacklisted names, cleans it against a file with irrelevant names and contents
* Then implements a strict find against a query name,
* If no results are found, a fuzzy search using Levenshtein distance is implemented and nearest results are reported

# Set up:
![ProgramFlow](https://cloud.githubusercontent.com/assets/5417573/21274782/8f3c8df0-c3d2-11e6-9514-a78e12a7b558.png)

# Details
* file has one name in every row (no XML, JSON,.., formatting)
* acceptable filetypes: txt, csv, tsv

# Tech used:
* Python 2.7
* Lubuntu 16.04

# Current issues:
* every time a name is queried, data is reimported and processed
* * In reality, a cronjob would do it in every X amount of time
* Partial matches are not ordered
* User raw input is not cleaned