import typing
from aoc.object_types import Solution
from aoc.utilities import transpose

# --- Day 4: Ceres Search ---
# Source: https://adventofcode.com/2024/day/4


def count_cross_mas_instances(word_search: typing.List[str]) -> int:
    configurations = [
        "MSMS",
        "SSMM",
        "MMSS",
        "SMSM",
    ]
    count = 0
    length = len(word_search)
    for i in range(1, length - 1):
        for j in range(1, length - 1):
            if word_search[i][j] == "A":
                corners = (
                    word_search[i - 1][j - 1]
                    + word_search[i - 1][j + 1]
                    + word_search[i + 1][j - 1]
                    + word_search[i + 1][j + 1]
                )
                if corners in configurations:
                    count += 1
    return count


def count_xmas_instances(word_search: typing.List[str]) -> int:
    line_variations = []
    line_variations += word_search[:]
    line_variations += transpose(matrix=word_search)
    line_variations += generate_diagonals(word_search=word_search)

    count = 0
    for line in line_variations:
        count += line.count("XMAS")
        count += line.count("SAMX")

    return count


def generate_diagonals(word_search: typing.List[str]) -> typing.List[str]:
    length = len(word_search)
    lines = []
    # TODO: Skip duplicate cross sections during loop
    for i in range(length):
        idxs = sorted(
            {(x, y) for x in range(i, -1, -1) for y in range(0, i + 1) if x + y == i}, reverse=True
        )
        lines.append("".join([word_search[x][y] for x, y in idxs]))
        lines.append("".join([word_search[length - x - 1][length - y - 1] for x, y in idxs]))
        lines.append("".join([word_search[x][length - y - 1] for x, y in idxs]))
        lines.append("".join([word_search[length - x - 1][y] for x, y in idxs]))

    return lines[:-3] + [lines[-1]]  # Remove duplicate cross-sections


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=count_xmas_instances(word_search=puzzle_input),
        second=count_cross_mas_instances(word_search=puzzle_input),
    )
