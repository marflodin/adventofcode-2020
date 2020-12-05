with open('../resources/input_day_1.txt', 'r') as input_file:
    numbers = []
    for line in input_file.readlines():
        numbers.append(int(line.strip()))

if __name__ == "__main__":
    for first_number in numbers:
        for second_number in numbers:
            for third_number in numbers:
                if first_number + second_number + third_number == 2020:
                    print(f"first_number {first_number}, second_number {second_number} and third_number {third_number} "
                          f"giving sum {first_number * second_number * third_number}")
