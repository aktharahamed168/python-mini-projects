import json


def format_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n===== Formatted JSON =====\n")

        print(json.dumps(data, indent=4))

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Invalid JSON format.")


print("===== JSON Formatter =====")

filename = "sample.json"

format_json(filename)
