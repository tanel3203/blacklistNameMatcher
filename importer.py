"""
Input: None
Output: raw imported file contents
Purpose: Get raw data from file
Methods (1):
        import_file(1 argument type textfile)
"""

# File import
def import_file(filename): 
    try:
        my_file = open(filename)
        my_doc = my_file.read()
    except:
        my_doc = ""

    return my_doc