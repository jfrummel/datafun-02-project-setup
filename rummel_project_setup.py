"""
Module: rummel_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Jeremy Rummel

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
from pathlib import Path
import time

# Import local modules
# TODO: Change this to import your module and uncomment
import utils_rummel 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    for year in range(start_year, end_year+1):
       #create path object
       year_folder = project_path.joinpath(str(year))
       #create folder
       year_folder.mkdir(exist_ok=True)
       # Log the function call and its arguments using an f-string
       print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
    # TODO: Add docstring
    """ Create folders from a list
    Arguments:
       folder_list = a list to be made into folders
       to_lowercase = makes all lowercase if True
       remove_spaces = removes spaces if True
    """
    # TODO: Log the function call and its arguments
    for item in folder_list:
        if to_lowercase & remove_spaces:
            item = item.lower().replace(" ", "")
        elif to_lowercase:
            item = item.lower()
        elif remove_spaces:
            item = item.replace(" ",)
        item_folder = project_path.joinpath(item)
        item_folder.mkdir(exist_ok=True)

        print(f"FUNCTION CALLED: create_folders_fom_list with {item_folder}")

    # TODO: Implement this function and remove the temporary pass
    pass


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    """ Function that creates folders with a list that adds a prefix
        Args:
          folder_list = a list of items to create folders
          prefix = prefix to be added to folder name
    """
    for item in folder_list:
        new_name = f"{prefix}{item}"
        item_folder = project_path.joinpath(new_name)
        item_folder.mkdir(exist_ok=True)

        print(f"FUNCTION CALLED: create_folders_fom_list with {item_folder}")
    

    # TODO: Implement this function professionally and remove the temporary pass
    pass

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    pass
    """Create folders periodically after the duration 
        Args:
          duration_seconds = number of seconds to wait for folder creation
    """
    for i in range(duration_seconds):
        folder_name = project_path.joinpath(f'Folder-{i+1}')
        folder_name.mkdir(exist_ok=True)
        time.sleep(duration_seconds)
        print(f'FUNCTION CALLED: create_folders_periodically with {folder_name}')
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    print(f"Byline: {utils_rummel.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5 # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended