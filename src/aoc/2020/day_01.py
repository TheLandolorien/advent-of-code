import math
import typing
from itertools import combinations

from aoc.object_types import Solution

# --- Day 1: Report Repair ---
# Source: https://adventofcode.com/2020/day/1


def find_product_of_2020_addends(
    expense_report: typing.List[str], count: int = 2
) -> typing.Union[int, None]:
    for addends in combinations(expense_report, count):
        if sum(addends) == 2020:
            return math.prod(addends)

    return None


def parse_puzzle(input: typing.List[str]) -> typing.List[int]:
    return [int(n) for n in input]


def solve(puzzle_input: typing.List[str]) -> Solution:
    expense_report = parse_puzzle(input=puzzle_input)

    return Solution(
        first=find_product_of_2020_addends(expense_report=expense_report),
        second=find_product_of_2020_addends(expense_report=expense_report, count=3),
    )
