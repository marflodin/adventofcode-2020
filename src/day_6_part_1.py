with open('../resources/input_day_6.txt', 'r') as input_file:
    entries = []
    entry = set()
    for line in input_file.readlines():
        if line in ['\n', '\r\n']:
            entries.append(entry)
            entry = set()
        else:
            for element in range(0, len(line.strip())):
                entry.add(line[element])
    entries.append(entry)


if __name__ == "__main__":
    result = 0
    for item in entries:
        result += len(item)
    print(f"result: {result}")