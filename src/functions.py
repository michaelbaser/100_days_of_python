
#--------
# Functions
#--------

from pathlib import Path

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