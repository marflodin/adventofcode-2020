with open('../resources/input_day_5.txt', 'r') as input_file:
    entries = []
    for line in input_file.readlines():
        entries.append(line.strip())


def get_seat_id(value: str) -> int:
    value = value.replace("B", "1")\
        .replace("F", "0")\
        .replace("R", "1")\
        .replace("L", "0")
    return int(value, 2)


if __name__ == "__main__":
    taken_seats = {}
    for entry in entries:
        taken_seats.update({get_seat_id(entry):None})
    print(f"max seat id: {max(list(taken_seats.keys()))}")
    index = 1
    while index < max(list(taken_seats.keys())):
        if not taken_seats.__contains__(index) and taken_seats.__contains__(index - 1) and taken_seats.__contains__(index + 1):
            print(f"Your seat: {index}")
        index += 1