import os
import hashlib


def calculate_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if not os.path.isfile(file_path):
            continue

        file_hash = calculate_hash(file_path)

        if file_hash in hashes:
            duplicates.append(
                (hashes[file_hash], filename)
            )
        else:
            hashes[file_hash] = filename

    return duplicates


print("===== Duplicate File Finder =====")

folder = "sample_files"

duplicates = find_duplicates(folder)

print("\nDuplicates Found")
print("-----------------")

if duplicates:

    for original, duplicate in duplicates:
        print(f"{original} = {duplicate}")

else:
    print("No duplicate files found.")
