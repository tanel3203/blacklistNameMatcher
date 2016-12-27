# Blacklist Name Matcher

## Description:
* If using a file: Imports a file with a list of blacklisted names, cleans it against a file with irrelevant names and contents
* If using EUROPA sanctions list: Imports XML from EUROPA sanctions list, processes it to list type
* Then implements a strict find against a query name,
* If no results are found, a modified (partial) search is implemented

## Contents
### Components:
* scraper.py (1 method)
* importer.py (1 method)
* processor.py (1 method)
* cleaner.py (1 method)
* terrorist_finder.py (3 methods)
* main.py

### Data:
* blacklist.tsv, blacklist.txt, ...
* noisefile.tsv, noisefile.txt, ...

## Example command line process
```
tanel@tanel:~/Documents/pyScript$ python main.py
Please enter name to search in the terrorist list 
> Robert Mugabe
Do you want to import a file or use the EUROPA database? (Input 'file', otherwise EUROPA is used) 
> europa
We will use the default sanctions list on ec.europa.eu and 8110 records (as at 27.12.2016)

Give it a few seconds...

------------------------------------------------------------------------------
IMPORTANT!
If this text is followed by an error
it is most likely you requested # names that's more than there are in the list
The list has  8110  existing names
------------------------------------------------------------------------------
No strict match, looking for partial matches...
TERRORIST MATCHED!
Certainty:  100.0 %
Name:  Robert Gabriel Mugabe

TERRORIST MATCHED!
Certainty:  100.0 %
Name:  Robert Gabriel Mugabe

TERRORIST MATCHED!
Certainty:  50.0 %
Name:  Grace Mugabe

TERRORIST MATCHED!
Certainty:  50.0 %
Name:  Grace Mugabe

TERRORIST MATCHED!
Certainty:  50.0 %
Name:  Robert Konars

```

## Program logic
![ProgramLogic](https://cloud.githubusercontent.com/assets/5417573/21502037/920f0464-cc55-11e6-998b-1b6ab22875c1.png)

## Program setup:
![ProgramSetUp](https://cloud.githubusercontent.com/assets/5417573/21502040/94a5c28a-cc55-11e6-9d41-a9ca784a58c9.png)

## Details
* file has one name in every row (no XML, JSON,.., formatting)
* common filetypes: txt, csv, tsv

## Tech used:
* Python 2.7
* Lubuntu 16.04

## Current issues:
* every time a name is queried, data is reimported and processed
* * In reality, a cronjob would do it in every X amount of time
* Partial matches are not ordered
* User raw input is not cleaned

# Content works, not yet implemented:
* (levenshteinDistance.py): fuzzy search using Levenshtein distance, if strict and partial matches don't return anything