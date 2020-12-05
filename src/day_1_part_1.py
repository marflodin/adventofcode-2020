with open('../resources/input_day_1.txt', 'r') as input_file:
    numbers = []
    for line in input_file.readlines():
        numbers.append(int(line.strip()))

if __name__ == "__main__":
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == 2020:
                print(f"first_number {first_number} and second_number {second_number} giving sum {first_number*second_number}")
                break