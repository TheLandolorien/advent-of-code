import typing
from aoc.object_types import Solution

# --- Day 4: Ceres Search ---
# Source: https://adventofcode.com/2024/day/4


def generate_all_line_variations(word_search: typing.List[str]) -> typing.List[str]:
    line_variations = []
    line_variations += word_search[:]
    line_variations += transpose_word_search(word_search=word_search)
    line_variations += generate_diagonals(word_search=word_search)

    count = 0
    for line in line_variations:
        count += line.count("XMAS")
        count += line.count("SAMX")

    return count


def transpose_word_search(word_search: typing.List[str]) -> typing.List[str]:
    transposition = []
    for i in range(len(word_search)):
        transposition.append("".join([line[i] for line in word_search]))
    return transposition


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
        first=generate_all_line_variations(word_search=puzzle_input),
        second=None,
    )
