import pytest


@pytest.mark.parametrize("example_number,example_solutions", [(1, (142, 142)), (2, (209, 281))])
def test_solve_with_numerical_digits_only(
    example_number,
    example_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[example_number - 1]
    mock_first, mock_second = example_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first, "should sum calibration values with digits only"
    assert second == mock_second, "should sum calibration values with number words"
