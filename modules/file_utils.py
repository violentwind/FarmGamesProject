import json
import os


def load_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def save_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
