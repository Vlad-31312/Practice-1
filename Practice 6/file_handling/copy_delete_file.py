import shutil
import os


shutil.copy("sample.txt", "sample_copy.txt")
print("File copied.")


shutil.copy("sample.txt", "backup.txt")
print("Backup created.")


if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("Copy deleted safely.")
else:
    print("File not found.")