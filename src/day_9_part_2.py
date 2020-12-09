with open('../resources/input_day_9.txt', 'r') as input_file:
    entries = {}
    index = 0
    for line in input_file.readlines():
        entries.update({index: int(line)})
        index += 1


def is_sum_of_number(start_index: int) -> int:
    answer_to_find = 776203571
    current_sum = 0
    for current_index in range(start_index, len(entries)):
        current_sum += entries[current_index]
        if current_sum == answer_to_find:
            return current_index
        elif current_sum > answer_to_find:
            return -1
    return -1


if __name__ == "__main__":
    result = 0
    for entry in entries.keys():
        end_index = is_sum_of_number(entry)
        if end_index != -1:
            print(f"start_index: {entry} end_index: {end_index}")
            break
    min_max_list = []
    for index in range(entry, end_index):
        min_max_list.append(entries[index])
    print(f"min: {min(min_max_list)} max: {max(min_max_list)} sum: {min(min_max_list) + max(min_max_list)}")