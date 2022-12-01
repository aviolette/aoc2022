from src.elves import group_lines_int


def which_elf(file: str):
    top_combined_scores(file, 1)


def top_combined_scores(file: str, num_elves: int):
    max_elves = []
    for items in group_lines_int(file):
        max_elves.append(sum(items))
        max_elves.sort()
        max_elves = max_elves[-num_elves:]

    print(sum(max_elves))


if __name__ == "__main__":
    # which_elf("example1.txt")
    which_elf("puzzle1.txt")
    top_combined_scores("puzzle1.txt", 3)
