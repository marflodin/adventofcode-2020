import copy

with open('../resources/input_day_8.txt', 'r') as input_file:
    entries = {}
    index = 0
    for line in input_file.readlines():
        bag_split = line.split(' ')
        entries.update({index: {'instruction': bag_split[0], 'value': int(bag_split[1]), 'visited': False}})
        index += 1


def handle_instruction(entries_copy, index: int):
    instruction = entries_copy[index]['instruction']
    entries_copy[index]['visited'] = True
    if instruction == 'acc':
        return {'new_index': index+1, 'acc': entries_copy[index]['value']}
    elif instruction == 'jmp':
        return {'new_index': index + entries_copy[index]['value'], 'acc': 0}
    elif instruction == 'nop':
        return {'new_index': index+1, 'acc': 0}


def find_correct_replacement(entries_copy):
    index = 0
    result = 0
    while 1 != 2:
        if index == 591 or entries_copy[index]['visited']:
            break
        instruction = handle_instruction(entries_copy, index)
        result += int(instruction['acc'])
        index = instruction['new_index']
    if index == 591:
        return result
    else:
        return -1


if __name__ == "__main__":
    result = -1
    for entry in entries.keys():
        entries_copy = copy.deepcopy(entries)
        if entries_copy[entry]['instruction'] == 'jmp':
            entries_copy[entry]['instruction'] = 'nop'
            result = find_correct_replacement(entries_copy)
        elif entries_copy[entry]['instruction'] == 'nop':
            entries_copy[entry]['instruction'] = 'jmp'
            result = find_correct_replacement(entries_copy)
        else:
            pass
        if result != -1:
            break
    print(f"result {result}")