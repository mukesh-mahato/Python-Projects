import os
import shutil

# Define the directory to be organized
directory = "/path/to/directory"

# Define the categories to sort files into
categories = {
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".jpg": "Image Files",
    ".mp3": "Music Files",
    ".mp4": "Video Files"
}

# Create the folders for each category
for category in categories.values():
    if not os.path.exists(os.path.join(directory, category)):
        os.mkdir(os.path.join(directory, category))

# Sort files into their respective categories
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1]
        if file_ext in categories:
            category_folder = os.path.join(directory, categories[file_ext])
            shutil.move(file_path, os.path.join(category_folder, file_name))
