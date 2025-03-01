#!/bin/bash
# filepath: /Users/diegofranciscolunalopez/Documents/42course/Python-Django-1-Librairies/ex01/my_script.sh

# Display pip version
echo "Pip version:"
python3 -m pip --version

# Create local_lib directory if it doesn't exist
mkdir -p local_lib

# Install path.py from GitHub to local_lib
# Force reinstall if it already exists
echo "Installing path.py from GitHub..."
python3 -m pip install --force-reinstall -t local_lib git+https://github.com/jaraco/path.git > install_path.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "path.py installed successfully. See install_path.log for details."
    
    # Execute Python program
    echo "Executing my_program.py..."
    python3 my_program.py
else
    echo "Failed to install path.py. See install_path.log for details."
    exit 1
fi