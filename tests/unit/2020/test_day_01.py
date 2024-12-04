import pytest

from unittest.mock import patch


@pytest.mark.parametrize("example_number,example_solutions", [(1, (514579, 241861950))])
def test_solve_calculates_puzzle_answers(
    example_number,
    example_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[example_number - 1]
    mock_first, mock_second = example_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)
    assert first == mock_first
    assert second == mock_second


def test_should_return_none_if_no_2020_addends(puzzle_module):
    with patch.object(puzzle_module.math, "prod") as mock_prod:
        result = puzzle_module.find_product_of_2020_addends(expense_report=[1, 2])
        mock_prod.assert_not_called()

    assert result is None, "should not multiply if no sums are 2020"
