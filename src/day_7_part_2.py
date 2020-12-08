import re

with open('../resources/input_day_7.txt', 'r') as input_file:
    entries = {}
    for line in input_file.readlines():
        bag_split = line.split('bags contain')
        contained_bags = bag_split[1].split(',')
        bag_entry = {}
        if bag_split[1].strip() == 'no other bags.':
            entries.update({bag_split[0].strip(): None})
        else:
            for contained_bag in contained_bags:
                try:
                    match = re.match(r"([0-9]+ )([a-z ]+)", contained_bag.strip(), re.I).groups()
                except:
                    print(f"failed to split {contained_bag.strip()}")
                bag_entry.update({
                    match[1].split('bag')[0].strip() : int(match[0].strip())
                })
            entries.update({bag_split[0].strip(): bag_entry})


def number_of_bags(bag_colour: str, inc_multiplier: int) -> int:
    print(f"bag_colour: {bag_colour} inc_multiplier: {inc_multiplier}")
    result = 0
    bags = entries.get(bag_colour, {})
    if bags is None:
        print(f"end of road on: {bag_colour} inc_multiplier: {inc_multiplier}")
        return inc_multiplier
    for bag in bags:
        multiplier = bags[bag]
        if bag_colour != 'shiny gold':
            result += inc_multiplier
        result += number_of_bags(bag, inc_multiplier*multiplier)
    return result


if __name__ == "__main__":
    print(f"result {number_of_bags('shiny gold', 1)}")