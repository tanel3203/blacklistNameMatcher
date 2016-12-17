# Blacklist Name Matcher

## Description:
* Imports a file with a list of blacklisted names, cleans it against a file with irrelevant names and contents
* Then implements a strict find against a query name,
* If no results are found, a modified (partial) search is implemented

## Contents
### Components:
* importer.py (1 method)
* processor.py (1 method)
* cleaner.py (1 method)
* terroristFinder.py (3 methods)
* main.py

### Data:
* blacklist.tsv, blacklist.txt, ...
* noisefile.tsv, noisefile.txt, ...

## Example command line process
```
tanel@tanel:~/Documents/pyBlacklist$ python main.py

Please enter name to search in the terrorist list 
> Obama Bin Laden
Please enter name of blacklist file in same path (e.g. blacklist.tsv) or absolute location 
> blacklist.tsv
Please enter name of noise file in same path (e.g. noisefile.tsv) or absolute location 
> noisefile.tsv
No strict match, looking for partial matches...
TERRORIST MATCHED!
Certainty:  33.33 %
Name:  Osama Laden

TERRORIST MATCHED!
Certainty:  66.67 %
Name:  Osama Bin Laden

TERRORIST MATCHED!
Certainty:  66.67 %
Name:  Bin Laden, Osama

TERRORIST MATCHED!
Certainty:  66.67 %
Name:  Laden Osama Bin

TERRORIST MATCHED!
Certainty:  66.67 %
Name:  osama bin laden

TERRORIST MATCHED!
Certainty:  66.67 %
Name:  osama and bin laden
```

## Set up:
![ProgramFlow](https://cloud.githubusercontent.com/assets/5417573/21275441/85653a40-c3d5-11e6-866a-c3029029aace.png)

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
* Implement a fuzzy search using Levenshtein distance, if strict and partial matches don't return anything