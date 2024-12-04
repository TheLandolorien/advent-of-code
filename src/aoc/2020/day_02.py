import typing
import re

from aoc.object_types import Solution

# --- Day 2: Password Philosophy ---
# Source: https://adventofcode.com/2020/day/2


def count_valid_password(password_list: typing.List[str], by_position: bool = False) -> int:
    password_validation_pattern = re.compile(pattern=r"(\d+)-(\d+) (\w): (.+)")
    validation_method = is_valid_password_by_position if by_position else is_valid_password_by_count
    results = []

    for line in password_list:
        num_1, num_2, match, password = password_validation_pattern.match(line).group(1, 2, 3, 4)
        num_1 = int(num_1)
        num_2 = int(num_2)
        results.append(validation_method(num_1, num_2, match, password))

    return results.count(True)


def is_valid_password_by_position(
    position_1: int,
    position_2: int,
    expected_char: str,
    password: str,
) -> bool:
    char_1 = password[position_1 - 1]
    char_2 = password[position_2 - 1]

    return (char_1 == expected_char or char_2 == expected_char) and char_1 != char_2


def is_valid_password_by_count(
    min_count: int, max_count: int, expected_char: str, password: str
) -> bool:
    occurrences = password.count(expected_char)

    return occurrences >= min_count and occurrences <= max_count


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=count_valid_password(password_list=puzzle_input),
        second=count_valid_password(password_list=puzzle_input, by_position=True),
    )
