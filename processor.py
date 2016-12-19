"""
Input: raw imported file
Output: list type processed data
Purpose: Process raw data to a manageable form
Methods (1):
        process_file(1 argument type textfile)
           expected: one row contains one value
"""

import importer as importer

# File processor
def process_file(filename):
    # Get file contents
    imported_file = importer.import_file(filename)

    # Add data to list
    # \n - newline
    processed_list = imported_file.split("\n")

    return processed_list