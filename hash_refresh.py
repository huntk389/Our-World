import os
import hashlib
import json

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

index = {}
for filename in os.listdir("story"):
    if filename.endswith(".txt"):
        path = os.path.join("story", filename)
        index[filename] = sha256_file(path)

with open("Integrity_Index.json", "w") as f:
    json.dump(index, f, indent=2)

print("SHA-256 hashes refreshed.")
