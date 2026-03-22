import os
from pathlib import Path

# find path from root
path = Path(__file__).resolve().parent

# Create folders
for number in range(1, 101):
    folder_name = f"day{'%02d' % number}"
    
    full_path = os.path.join(path, folder_name)
    
    
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Folder created: {full_path}")
    else:
        print(f"Folder already exists so not overwritten: {full_path}")


