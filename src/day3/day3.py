from src.elves import groups_of, strip_lines

values = {}


def weight(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def puzzle1(file_name):
    count = 0
    for line in strip_lines(file_name):
        half = int(len(line) / 2)
        comp1, comp2 = line[0: half], line[half:]
        items = {a for a in comp1}.intersection({b for b in comp2})
        t = sum([weight(item) for item in items])
        count += t
    print(count)


def puzzle2(file_name):
    priority = 0
    for lines in groups_of(file_name, 3):
        print(lines)
        i1 = {a for a in lines[0]}.intersection({b for b in lines[1]})
        i2 = {c for c in lines[2]}.intersection(i1)
        priority += sum([weight(item) for item in i2])
    print(priority)


if __name__ == "__main__":
    # puzzle1("example1.txt")
    # puzzle1("puzzle1.txt")
    puzzle2("puzzle1.txt")
