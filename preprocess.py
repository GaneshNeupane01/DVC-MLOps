import os
with open("large_files/demoOfLargefile.txt") as f:
    split_words = f.read().split()

processed = [x.lower() for x in split_words]
os.makedirs("data", exist_ok=True)
with open("data/processed.txt", "w") as f:
    for x in processed:
        f.write(f"{x}\n")
