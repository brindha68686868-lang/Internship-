import os
import shutil
from datetime import datetime

# Source and backup folders
source_folder = r"D:\MyFiles"
backup_folder = r"D:\Backups"

# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create backup directory
backup_path = os.path.join(backup_folder, f"backup_{timestamp}")
os.makedirs(backup_path, exist_ok=True)

# Copy files
for file_name in os.listdir(source_folder):
    source_file = os.path.join(source_folder, file_name)

    if os.path.isfile(source_file):
        shutil.copy2(source_file, backup_path)

print(f"Backup completed successfully!")
print(f"Backup location: {backup_path}")