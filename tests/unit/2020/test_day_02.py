import pytest


@pytest.mark.parametrize("example_number,example_solutions", [(1, (2, None))])
def test_solve_calculates_puzzle_answers(
    example_number,
    example_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[example_number - 1]
    mock_first, mock_second = example_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first, "should count valid password"
    assert second == mock_second, "should <PART_2_SCENARIO>"
