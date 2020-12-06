import re
from typing import Optional

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


def is_valid_height(value: str) -> bool:
    if value is None:
        return False
    try:
        match = re.match(r"([0-9]+)([a-z]+)", value, re.I).groups()
    except AttributeError:
        return False
    if match[1] == 'cm':
        return is_between(int(match[0]), 150, 193)
    elif match[1] == 'in':
        return is_between(int(match[0]), 59, 76)
    else:
        return False


def is_valid_colour(value: str) -> bool:
    if value is None:
        return False
    try:
        match = re.match(r"(#)([a-z0-9]+)", value, re.I).groups()
    except AttributeError:
        return False
    return len(match) == 2 and len(match[1]) == 6


def is_valid_eye_colour(value: str) -> bool:
    if value is None:
        return False
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_between(value: int, min: int, max: int) -> bool:
    if value is None:
        return False
    return min <= value <= max


def is_valid_passport_id(value: str) -> bool:
    if value is None:
        return False
    return len(value) == 9 and value.isdigit()


def safely_get_int(value: str) -> Optional[int]:
    try:
        return int(value)
    except:
        return None


def is_valid_passport(item) -> bool:
    required_keys_map = {
        'byr': {is_between(value=safely_get_int(item.get('byr', None)), min=1920, max=2002)},
        'iyr': {is_between(value=safely_get_int(item.get('iyr', None)), min=2010, max=2020)},
        'eyr': {is_between(value=safely_get_int(item.get('eyr', None)), min=2020, max=2030)},
        'hgt': {is_valid_height(value=item.get('hgt', None))},
        'hcl': {is_valid_colour(value=item.get('hcl', None))},
        'ecl': {is_valid_eye_colour(value=item.get('ecl', None))},
        'pid': {is_valid_passport_id(value=item.get('pid', None))}
    }
    for key in required_keys_map:
        if not next(iter(required_keys_map[key])):
            print(f"invalid key {key} for element {item}")
            return False
    return True


if __name__ == "__main__":
    valid_passports = 0
    for entry in entries:
        if is_valid_passport(entry):
            valid_passports += 1
    print(f"Valid passports {valid_passports}")
    print(f"passports {len(entries)}")
