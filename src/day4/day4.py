from src.elves import strip_lines


def int_range(range1):
    return [int(x) for x in range1.split("-")]


def contains(range1, range2):
    return range1[0] <= range2[0] and range1[1] >= range2[1]


def overlap(range1, range2):
    return (range1[0] <= range2[0] <= range1[1]) or (range2[0] <= range1[0] <= range2[1])


def puzzle1(file_name):
    count = 0
    for line in strip_lines(file_name):
        range1, range2 = line.split(",")
        range1, range2 = int_range(range1), int_range(range2)
        if contains(range1, range2) or contains(range2, range1):
            count += 1
    print(count)


def puzzle2(file_name):
    count = 0
    for line in strip_lines(file_name):
        range1, range2 = line.split(",")
        range1, range2 = int_range(range1), int_range(range2)
        if overlap(range1, range2):
            count += 1
    print(count)


if __name__ == "__main__":
    # puzzle1("example1.txt")
    # puzzle1("puzzle1.txt")
    # puzzle2("example1.txt")
    puzzle2("puzzle1.txt")