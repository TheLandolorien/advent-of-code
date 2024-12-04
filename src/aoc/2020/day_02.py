import typing
import re

from aoc.object_types import Solution

# --- Day 2: Password Philosophy ---
# Source: https://adventofcode.com/2020/day/2


def count_valid_password(password_list: typing.List[str]) -> int:
    return [is_valid_password(line) for line in password_list].count(True)


def is_valid_password(line: str) -> bool:
    password_validation_pattern = re.compile(pattern=r"(\d+)-(\d+) (\w): (.+)")
    min_count, max_count, char, password = password_validation_pattern.match(line).group(1, 2, 3, 4)
    min_count = int(min_count)
    max_count = int(max_count)

    occurrences = password.count(char)

    return occurrences >= min_count and occurrences <= max_count


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=count_valid_password(password_list=puzzle_input),
        second=None,
    )
