import os
from pathlib import Path

# find path from root
path = Path(__file__).resolve().parent

# make sure correct path
print(path)


# Create folder as 'Day xx -' e.g. 'Day 01 -' in specified folderpath
for number in range(10, 11):
    folder_name = f"day{'%02d' % number}"
    
    full_path = os.path.join(path, folder_name)
    
    
    # Create the directory
    try:
            os.makedirs(full_path, exist_ok=True) 
            print(f"Created: {folder_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f'Folder created: {full_path}')
