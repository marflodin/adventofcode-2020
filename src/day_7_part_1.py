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


def contains_colour(bag_colour: str) -> bool:
    if bag_colour is None:
        return False
    elif bag_colour == 'shiny gold':
        return True
    elif entries.get(bag_colour, {}) is None:
        return False
    else:
        for colour in entries.get(bag_colour, {}):
            try:
                if colour is not None and contains_colour(colour):
                    return True
            except:
                print(f"error: {colour}")
        return False


if __name__ == "__main__":
    result = set()
    for bag_colour in entries.keys():
        if bag_colour is None:
            continue
        elif bag_colour == 'shiny gold':
            continue
        elif contains_colour(bag_colour):
            result.add(bag_colour)
    print(f"result {len(result)}")