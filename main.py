import os
import hashlib


def get_file_hash(filepath):
    """Return MD5 hash of file"""
    hasher = hashlib.md5()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(path)

                if file_hash in hashes:
                    duplicates.append((path, hashes[file_hash]))
                else:
                    hashes[file_hash] = path

            except:
                pass

    return duplicates


folder = input("Enter folder path: ")

dups = find_duplicates(folder)

if not dups:
    print("No duplicate files found.")
else:
    print("\nDuplicate files:")
    for file1, file2 in dups:
        print(file1)
        print("duplicate of")
        print(file2)
        print("-" * 40)
