import os
import shutil
from datetime import datetime

def organize_by_type(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1][1:]  # Get file extension
            target_folder = os.path.join(directory, file_extension.upper())
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
    print("Files organized by type.")

def organize_by_date(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            target_folder = os.path.join(directory, date_folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
    print("Files organized by date.")

def main():
    print("File Organizer")
    print("1. Organize by Type")
    print("2. Organize by Date")
    choice = input("Choose an option: ")
    directory = input("Enter the directory to organize: ")

    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    if choice == '1':
        organize_by_type(directory)
    elif choice == '2':
        organize_by_date(directory)
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()