import os
import shutil

# Folder path (change this to your Downloads folder)
folder_path = "first"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
}

# Create folders if they don't exist
for folder in file_types.keys():
    path = os.path.join(folder_path, folder)
    if not os.path.exists(path):
        os.makedirs(path)

# Create Others folder
others_path = os.path.join(folder_path, "Others")
if not os.path.exists(others_path):
    os.makedirs(others_path)

# Scan files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(others_path, file))

print("Files organized successfully!")