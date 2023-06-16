import os

# list the files and folders in the current directory
files_folders = os.listdir()

# check if the "export" folder is in this directory
if "export" not in files_folders:
    print("Export folder not created yet")
    os.mkdir("export")
    print("✅ Export folder created")