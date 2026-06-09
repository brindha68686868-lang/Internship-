import os
import shutil

source_folder = r"C:\Users\ELCOT\Downloads"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1][1:]

        if extension:
            target_folder = os.path.join(source_folder, extension.upper())

            os.makedirs(target_folder, exist_ok=True)

            shutil.move(file_path,
                        os.path.join(target_folder, file))

print("Files organized successfully!")