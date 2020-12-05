def get_position_key(x: int, y: int) -> str:
    return f"{x}:{y}"


with open('../resources/input_day_3.txt', 'r') as input_file:
    items = {}
    y = 0
    for line in input_file.readlines():
        x = 0
        for element in range(0, len(line.strip())):
            item = {get_position_key(x, y): line[element]}
            items.update(item)
            x += 1
        y += 1
    print(f"{y} : {x}")


def traverse_slopes(steps_right: int, steps_down: int) -> int:
    trees = 0
    x_pos = 0
    y_pos = 0
    while y_pos <= y - 1:
        if items[get_position_key(x_pos % x, y_pos)] == '#':
            trees += 1
        x_pos += steps_right
        y_pos += steps_down
    return trees


if __name__ == "__main__":
    result = 1
    trees = []
    trees.append(traverse_slopes(1,1))
    trees.append(traverse_slopes(3,1))
    trees.append(traverse_slopes(5,1))
    trees.append(traverse_slopes(7,1))
    trees.append(traverse_slopes(1,2))
    for tree in trees:
        result = result * tree
    print(f"trees: {result}")