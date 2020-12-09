with open('../resources/input_day_9.txt', 'r') as input_file:
    entries = {}
    index = 0
    for line in input_file.readlines():
        entries.update({index: int(line)})
        index += 1


def is_sum_of_previous_numbers(index: int) -> bool:
    if index < 25:
        return True
    entry_to_validate = int(entries[index])
    for first_num_index in range(index- 25, index):
        for second_num_index in range(index - 25, index):
            if first_num_index == second_num_index:
                pass
            elif entries[first_num_index] + entries[second_num_index] == entry_to_validate:
                return True
    return False


if __name__ == "__main__":
    result = 0
    for entry in entries.keys():
        if not is_sum_of_previous_numbers(entry):
            print(f"entry: {entry} with value: {entries[entry]}")
            break
