from src.elves import strip_lines

ROCK_1 = 'A'
ROCK_2 = 'X'
PAPER_1 = 'B'
PAPER_2 = 'Y'
SCISSORS_1 = 'C'
SCISSORS_2 = 'Z'

scores = {
    ROCK_1: 1,
    ROCK_2: 1,
    PAPER_1: 2,
    PAPER_2: 2,
    SCISSORS_1: 3,
    SCISSORS_2: 3
}

wins = {
    # rock => scissors
    ROCK_2: SCISSORS_1,
    ROCK_1: SCISSORS_2,
    # paper => rock
    PAPER_2: ROCK_1,
    PAPER_1: ROCK_2,
    # scissors =>  paper
    SCISSORS_2: PAPER_1,
    SCISSORS_1: PAPER_2
}

loses = {v: k for k, v in wins.items()}


def rcb(theirs: str, yours: str) -> int:
    if scores[theirs] == scores[yours]:
        return 3 + scores[yours]
    elif wins[yours] == theirs:
        return 6 + scores[yours]
    return 0 + scores[yours]


def score_from_outcome(theirs: str, outcome: str) -> int:
    match outcome:
        case 'X':
            return rcb(theirs, wins[theirs])
        case 'Y':
            return rcb(theirs, theirs)
        case 'Z':
            return rcb(theirs, loses[theirs])


def run_program(file_name, score_it):
    count = 0
    for play in strip_lines(file_name):
        count += score_it(*play.split(" "))
    print(count)


if __name__ == "__main__":
    run_program("puzzle1.txt", rcb)
    run_program("example1.txt", score_from_outcome)
    run_program("puzzle1.txt", score_from_outcome)
