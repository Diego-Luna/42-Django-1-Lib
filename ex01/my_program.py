import sys
import os

# Add local_lib directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
local_lib_path = os.path.join(current_dir, 'local_lib')
sys.path.insert(0, local_lib_path)

# Import path module from local_lib
try:
    from path import Path
except ImportError:
    print("Error: Cannot import path module. Make sure it's installed correctly.")
    sys.exit(1)

def main():
    print("Starting my_program.py...")
    
    # Create a folder
    folder_name = "new_folder"
    new_folder = Path(folder_name)
    
    if not new_folder.exists():
        print(f"Creating folder: {folder_name}")
        new_folder.mkdir()
    else:
        print(f"Folder {folder_name} already exists")
    
    # Create a file inside the folder
    file_path = new_folder / "new_file.txt"
    
    # Write content to the file
    message = "This file was created by my_program.py using path.py!\n"
    message += "Python-Django - 1 Librairies Exercise 01"
    
    print(f"Writing to file: {file_path}")
    file_path.write_text(message)
    
    # Read and display file content
    print("\nReading file content:")
    content = file_path.read_text()
    print("-" * 50)
    print(content)
    print("-" * 50)
    
    print("Program completed successfully!")

if __name__ == "__main__":
    main()