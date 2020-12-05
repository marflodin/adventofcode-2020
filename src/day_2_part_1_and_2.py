with open('../resources/input_day_2.txt', 'r') as input_file:
    entries = []
    for line in input_file.readlines():
        character_condition = line.split(':')[0]
        entries.append({
            'password': line.split(':')[1].strip(),
            'needed_character': character_condition.split(' ')[1],
            'min_times': int(character_condition.split(' ')[0].split('-')[0]),
            'max_times': int(character_condition.split(' ')[0].split('-')[1])
        })


def valid_password(entry) -> bool:
    character_count = entry['password'].count(entry['needed_character'])
    return entry['min_times'] <= character_count <= entry['max_times']


def valid_password_v2(entry) -> bool:
    password = entry['password']
    expected_char = entry['needed_character']
    first_char = password[entry['min_times'] - 1]
    second_char = password[entry['max_times'] - 1]
    if first_char == expected_char:
        return second_char != expected_char
    else:
        return second_char == expected_char


if __name__ == "__main__":
    valid_passwords = 0
    for entry in entries:
        if valid_password_v2(entry):
            valid_passwords += 1
    print(f"{valid_passwords} valid passwords")
