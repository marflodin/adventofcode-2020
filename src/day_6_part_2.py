with open('../resources/input_day_6.txt', 'r') as input_file:
    entries = []
    entry = {"persons": 0}
    for line in input_file.readlines():
        if line in ['\n', '\r\n']:
            entries.append(entry)
            entry = {"persons": 0}
        else:
            entry["persons"] = entry["persons"] + 1
            for element in range(0, len(line.strip())):
                old_value = entry.get(line[element], 0)
                entry[line[element]] = old_value + 1
    entries.append(entry)


if __name__ == "__main__":
    result = 0
    for item in entries:
        for key in item:
            if key == "persons":
                pass
            elif item[key] == item["persons"]:
                result += 1
            else:
                pass
    print(f"result: {result}")