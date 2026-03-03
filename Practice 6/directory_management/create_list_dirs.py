import os

os.makedirs("test_folder/subfolder", exist_ok=True)


print("Содержимое test_folder:", os.listdir("test_folder"))


txt_files = [f for f in os.listdir("test_folder") if f.endswith(".txt")]
print("Текстовые файлы:", txt_files)