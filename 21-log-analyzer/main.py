from collections import Counter


def analyze_log(filename):
    levels = Counter()
    errors = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()

            if len(parts) < 4:
                continue

            level = parts[2]
            message = " ".join(parts[3:])

            levels[level] += 1

            if level == "ERROR":
                errors.append(message)

    return levels, errors


print("===== Log Analyzer =====")

filename = "sample.log"

levels, errors = analyze_log(filename)

print("\nLog Summary")
print("-----------")

for level, count in levels.items():
    print(f"{level}: {count}")

print("\nErrors Found")
print("------------")

if errors:
    for error in errors:
        print("-", error)
else:
    print("No errors found.")
