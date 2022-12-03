def strip_lines(file_name):
    for line in open(file_name, "r"):
        line = line.strip()
        yield line


def intlines(filename):
    for line in strip_lines(filename):
        yield int(line)


def stripsort(file_name, func):
    lines = [func(line) for line in strip_lines(file_name)]
    lines.sort()
    return lines


def group_lines(file_name, transform=lambda a: a):
    group = []
    for line in strip_lines(file_name):
        if len(line):
            group.append(transform(line))
        else:
            yield group
            group = []
    if group:
        yield group


def groups_of(file_name, num, transform=lambda a: a):
    group = []
    for i, line in enumerate(strip_lines(file_name)):
        if i != 0 and i % num == 0:
            yield group
            group = []
        group.append(transform(line))

    if group:
        yield group


def group_lines_int(file_name):
    return group_lines(file_name, lambda a: int(a))
