with open("data/data.txt") as f:
    nums = [int(x) for x in f]

processed = [x * 2 for x in nums]

with open("data/processed.txt", "w") as f:
    for x in processed:
        f.write(f"{x}\n")
