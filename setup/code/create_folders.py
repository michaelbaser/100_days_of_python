#--------
# Packages
#--------

import os
from pathlib import Path
import pandas as pd

#--------
# Functions
#--------

# Find root
def find_root_dir(target_dir_name):
    
    # Start from current dir
    current_dir = Path.cwd()
    
    # Look upwards until identify target directory
    for parent in current_dir.parents:
        # If the target exists, return
        if(parent / target_dir_name).exists():
            return parent / target_dir_name
        
    # If directory not found return 'None' to confirm
    return None
        
#--------
# Setup
#--------

# find path from root
root_dir = find_root_dir("100_days_of_python")

# project folder path
project_path = f'{root_dir}/Projects'

# Read data, drop index col
df = pd.read_csv(f'{root_dir}/setup/data/course_content.csv',index_col=0)
print(df)

#--------
# Create folders and files
#--------


# Create folders and readme files from day01-day100
for number in range(1, 101):
    
    # For finding folder name
    folder_name = f'day{'%02d' % number}'
    
    # For finding readme title name
    day_str = f"{number:02d}"
    
    # Full path for saving out to
    full_path = os.path.join(project_path, folder_name)
    
    
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        
        # Find the relevant module title using the number in range, then add to title
        module_name = df.loc[number, "Module"]                
        readme_title_name = f'Day {day_str} - {module_name}'
        
        # readme path generation 
        readme_path = os.path.join(full_path, "README.md")
        
        # Write readme file 
        with open(readme_path, "w") as f:
            f.write(f'## {readme_title_name}')
            
        print(f"Folder created: {full_path}")
    else:
        print(f"Folder already exists so not overwritten: {full_path}")


