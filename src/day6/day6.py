from src.elves import strip_lines


def packet_detect(message: str, chars: int):
    for i in range(chars, len(message)):
        if i < chars:
            continue
        window = message[i - chars: i]
        uniques = len({a for a in window})
        if uniques == chars:
            return i


def puzzle61(message: str):
    return packet_detect(message, 4)


def puzzle62(message: str):
    return packet_detect(message, 14)


if __name__ == "__main__":
    assert puzzle61("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert puzzle61("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert puzzle61("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert puzzle61("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    line = next(strip_lines("day6_p1.txt"))
    print(puzzle61(line))
    assert puzzle62("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert puzzle62("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert puzzle62("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert puzzle62("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert puzzle62("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    print(puzzle62(line))
