
import json

try:
    with open("logs.json", "r") as file:
        data = json.load(file)

    info = 0
    warning = 0
    error = 0

    print("All Log Records:")

    for record in data:
        print(record)

        if record["level"] == "INFO":
            info += 1
        elif record["level"] == "WARNING":
            warning += 1
        elif record["level"] == "ERROR":
            error += 1

    print("\nLog Summary:")
    print("INFO:", info)
    print("WARNING:", warning)
    print("ERROR:", error)

except FileNotFoundError:
    print("JSON file not found.")

except json.JSONDecodeError:
    print("Invalid JSON format.")
