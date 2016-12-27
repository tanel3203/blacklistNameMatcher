"""
Input: list type processed data
Output: 
Purpose: Remove irrelevant values from main file
Methods (1):
       cleaner(1-2 argument(s) type textfile)
"""

import processor as processor
import re

def cleaner(file_to_be_cleaned, noise_file_to_clean_with = []):

    # Define contents to be cleaned
    file_shiny = processor.process_file(file_to_be_cleaned)
    # Exit method if nothing to clean
    if (len(noise_file_to_clean_with) == 0): return file_shiny
    # Define noise to clean 
    file_noisy = processor.process_file(noise_file_to_clean_with)

    # Find noise in names 
    for index, name in enumerate(file_shiny):
        for noise in file_noisy:
            if (re.search(noise, name)):

                # Remove the noise and trim the string in file and current string 
                file_shiny[index] = name.replace(noise, "").strip()
                name = name.replace(noise, "").strip()
    

    return file_shiny