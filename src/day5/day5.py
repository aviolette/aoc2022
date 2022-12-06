import re


def arrange9000(stacks, num, from_stack, to_stack):
    source_stack = stacks[from_stack - 1]
    target_stack: list = stacks[to_stack - 1]
    for i in range(0, num):
        item = source_stack.pop(0)
        target_stack.insert(0, item)


def arrange9001(stacks, num, from_stack, to_stack):
    source_stack = stacks[from_stack - 1]
    target_stack: list = stacks[to_stack - 1]
    items = source_stack[0:num]
    stacks[from_stack - 1] = source_stack[num:]
    stacks[to_stack - 1] = items + target_stack


def crane(file_name, arrange):
    stacks = []
    built = False
    for line in open(file_name, "r"):
        line = line.rstrip()
        if not built:
            if "[" in line:
                j = 0
                for i in range(1, len(line), 4):
                    if len(stacks) <= j:
                        stacks.append([])
                    column = stacks[j]
                    if line[i].isalpha():
                        column.append(line[i])
                    j += 1
            else:
                built = True
        else:
            m = re.search(r'move (\d+) from (\d+) to (\d+)', line)
            if m:
                arrange(stacks, int(m.group(1)), int(m.group(2)), int(m.group(3)))
    result = "".join([item[0] for item in stacks])

    print(result)


if __name__ == "__main__":
    # puzzle51("example5-1.txt")
    # crane("puzzle5-1.txt", arrange9000)
    # crane("example5-1.txt", arrange9001)
    crane("puzzle5-1.txt", arrange9001)
