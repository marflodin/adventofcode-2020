with open('../resources/input_day_4.txt', 'r') as input_file:
    entries = []
    entry = {}
    for line in input_file.readlines():
        if line in ['\n', '\r\n']:
            entries.append(entry)
            entry = {}
        else:
            properties = line.split(' ')
            for prop in properties:
                entry[prop.split(':')[0].strip()] = prop.split(':')[1].strip()
    entries.append(entry)

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid_passport(item) -> bool:
    for key in required_keys:
        if item.get(key, None) is None:
            return False
    return True


if __name__ == "__main__":
    valid_passports = 0
    for entry in entries:
        if is_valid_passport(entry):
            valid_passports += 1
    print(f"Valid passports {valid_passports}")
    print(f"passports {len(entries)}")
