import pytest
from main import get_bet, deposit, check_winnings, get_number_of_lines, symbol_value

# Test for test_get_bet
@pytest.mark.parametrize(
    "mock_inputs, expected_output",
    [
        (["50"], 50.00),  # Valid input
        (["abc", "50"], 50.00),  # Invalid first input, then valid
        (["0", "20"], 20.00),  # Out-of-range first input, then valid
        (["200", "100"], 100.00),  # Too high first input, then valid
    ],
)
def test_get_bet(monkeypatch, mock_inputs, expected_output):
    """Test the get_bet function with different input scenarios."""
    
    # Mock input() function to return values from the mock_inputs list
    monkeypatch.setattr("builtins.input", lambda _: mock_inputs.pop(0))

    # Call the function and assert expected result
    assert get_bet() == expected_output

# Test for deposit function
@pytest.mark.parametrize(
    "mock_inputs, expected_output",
    [
        (["100"], 100.0),  # Valid input
        (["xyz", "50"], 50.0),  # Invalid first input, then valid
        (["-10", "30"], 30.0),  # Negative first input, then valid
        (["0", "25"], 25.0),  # Zero first input, then valid
    ],
)
def test_deposit(monkeypatch, mock_inputs, expected_output):
    """Test deposit function with different input scenarios."""
    
    monkeypatch.setattr("builtins.input", lambda _: mock_inputs.pop(0))
    assert deposit() == expected_output

# Test for get_number_of_lines function
@pytest.mark.parametrize(
    "mock_inputs, expected_output",
    [
        (["3"], 3),  # Valid input
        (["xyz", "2"], 2),  # Invalid first input, then valid
        (["0", "1"], 1),  # Zero first input, then valid
        (["10", "3"], 3),  # Too high first input, then valid
    ],
)
def test_get_number_of_lines(monkeypatch, mock_inputs, expected_output):
    """Test get_number_of_lines function with different input scenarios."""

    monkeypatch.setattr("builtins.input", lambda _: mock_inputs.pop(0))
    assert get_number_of_lines() == expected_output

# Test for test_check_winnings function
@pytest.mark.parametrize(
    "columns, lines, bet, expected_winnings, expected_lines",
    [
        # ✅ Case 1: One winning line (A)
        (
            [["A", "C", "A"], ["A", "X", "Y"], ["A", "M", "N"]],
            3,
            10,
            50,  # 5 (A) * 10 (bet)
            [1]  # First row wins
        ),

        # ✅ Case 2: Two winning lines (A and B)
        (
            [["A", "B", "A"], ["A", "B", "B"], ["A", "B", "C"]],
            3,
            5,
            (5 * 5) + (4 * 5),  # A=25 + B=20
            [1, 2]  
        ),

        # ❌ Case 3: No winning lines
        (
            [["A", "B", "C"], ["X", "Y", "Z"], ["L", "M", "N"]],
            3,
            10,
            0,  
            []
        ),

        # ✅ Case 4: Different bet with winning row (C)
        (
            [["C", "B", "C"], ["C", "A", "A"], ["C", "A", "B"]],
            3,
            20,
            60,  # 3 (C) * 20
            [1]
        ),

        # ✅ Case 5: All rows win (A, B, C)
        (
            [["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]],
            3,
            10,
            (5 * 10) + (4 * 10) + (3 * 10),  # A=50, B=40, C=30
            [1, 2, 3]
        ),

        # 🔍 Edge Case 6: Single column only
        (
            [["A"], ["A"], ["A"]],
            1,
            10,
            50,  # A * 10
            [1]
        ),

        # 🔍 Edge Case 7: Empty grid (should return 0 winnings)
        (
            [],
            0,
            10,
            0,
            []
        ),

        # ⚠️ Edge Case 8: Symbols not in values (should return 0)
        (
            [["X", "X", "X"], ["Y", "Y", "Y"], ["Z", "Z", "Z"]],
            3,
            10,
            0,  # No valid symbols
            []
        ),
    ]
)
def test_check_winnings(columns, lines, bet, expected_winnings, expected_lines):
    """Test check_winnings with different scenarios."""
    
    winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
    
    assert winnings == expected_winnings, f"Expected {expected_winnings}, got {winnings}"
    assert winning_lines == expected_lines, f"Expected {expected_lines}, got {winning_lines}"