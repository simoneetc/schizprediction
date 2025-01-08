import os
from chardet import detect

project_path = "D:/schizprediction"
ignored_dirs = {"venv", ".venv", "__pycache__", "site-packages"}  # Add folders to exclude

for root, dirs, files in os.walk(project_path):
    # Remove ignored directories from traversal
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    raw_data = f.read()
                    encoding = detect(raw_data)['encoding']
                    if encoding != "utf-8":
                        print(f"{file_path} is encoded in {encoding}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
