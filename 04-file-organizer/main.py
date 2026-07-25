import os
import shutil

source_folder = "sample"

file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos"
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        folder_name = file_types.get(extension, "Others")

        destination = os.path.join(source_folder, folder_name)

        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully!")
