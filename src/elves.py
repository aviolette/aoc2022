def striplines(file_name):
    for line in open(file_name, "r"):
        line = line.strip()
        yield line


def intlines(filename):
    for line in striplines(filename):
        yield int(line)


def stripsort(file_name, func):
    lines = [func(line) for line in striplines(file_name)]
    lines.sort()
    return lines


def group_lines(file_name, transform=lambda a: a):
    group = []
    for line in striplines(file_name):
        if len(line):
            group.append(transform(line))
        else:
            yield group
            group = []
    if group:
        yield group


def group_lines_int(file_name):
    return group_lines(file_name, lambda a: int(a))
