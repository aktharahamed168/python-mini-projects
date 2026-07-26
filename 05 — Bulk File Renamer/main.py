import os

folder = r"C:\Users\aktha\OneDrive\Desktop\sample"

prefix = input("Enter new file name: ")

count = 1

for file in os.listdir(folder):
  file_path = os.path.join(folder, file)

  if os.path.isfile(file_path):
    extension = os.path.splitext(file)[1]
    new_name = f"{prefix}_{count}{extension}"
    new_path = os.path.join(folder, new_name)
    os.rename(file_path, new_path)
    print(f"{file} → {new_name}")
    count += 1

print("\nAll files renamed successfully!")
