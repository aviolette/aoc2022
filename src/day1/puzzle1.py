from src.elves import intlines, striplines


def which_elf(file: str):
    top_combined_scores(file, 1)


def top_combined_scores(file: str, num_elves: int):
    max_elves = []
    current_score = 0
    for line in striplines(file):
        if not line:
            max_elves.append(current_score)
            max_elves.sort()
            max_elves = max_elves[-num_elves:]
            current_score = 0
        else:
            current_score += int(line)

    print(sum(max_elves))


if __name__ == "__main__":
    # which_elf("example1.txt")
    which_elf("puzzle1.txt")
    top_combined_scores("puzzle1.txt", 3)
