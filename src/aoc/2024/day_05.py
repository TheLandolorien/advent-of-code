import typing
import copy
from functools import cmp_to_key
from aoc.object_types import Solution

# --- Day 5: Print Queue ---
# Source: https://adventofcode.com/2024/day/5


def sum_correctly_ordered_middle_pages(
    page_rules: typing.Dict[int, typing.List[int]],
    production_pages: typing.List[typing.List[int]],
) -> int:
    correct_middle_pages = []
    for manual_pages in production_pages:
        any_violation = False
        for idx, page in enumerate(manual_pages):
            if not set(manual_pages[idx + 1 :]).issubset(set(page_rules.get(page, []))):
                any_violation = True
                break
        if not any_violation:
            middle_page_number = manual_pages[len(manual_pages) // 2]
            correct_middle_pages.append(middle_page_number)
    return sum(correct_middle_pages)


def _parse_updates(
    rules_and_pages: typing.List[str],
) -> typing.Tuple[
    typing.Dict[int, typing.List[int]],
    typing.List[typing.List[int]],
]:
    section_divider_idx = rules_and_pages.index("")
    raw_rules = rules_and_pages[:section_divider_idx]
    raw_pages = rules_and_pages[section_divider_idx + 1 :]
    rules = {}
    for rule in raw_rules:
        before, after = rule.split("|")
        rules.setdefault(int(before), []).append(int(after))

    pages = [[int(x) for x in pages.split(",")] for pages in raw_pages]
    return rules, pages


def solve(puzzle_input: typing.List[str]) -> Solution:
    page_rules, production_pages = _parse_updates(rules_and_pages=puzzle_input)
    return Solution(
        first=sum_correctly_ordered_middle_pages(
            page_rules=page_rules,
            production_pages=production_pages,
        ),
        second=None,
    )
