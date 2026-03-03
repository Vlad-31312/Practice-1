import shutil
import os

if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "test_folder/sample.txt")
    print("sample.txt перемещён в test_folder")


shutil.copy("test_folder/sample.txt", "sample_copy.txt")
print("Файл скопирован обратно как sample_copy.txt")