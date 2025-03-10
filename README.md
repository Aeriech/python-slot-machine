### Project Overview - Python Slot Machine Simulator
This project is a Python-based slot machine simulator, designed for learning purposes. It helps understand randomization, user input handling, loops, conditionals, and function-based programming.

Key Features:
   - Deposit System - Users can deposit money to play.
   - Betting System - Users can select the number of lines to bet on and place bets within a defined limit.
   - Slot Machine Mechanics - Uses randomization to generate slot machine spins.
   - Winning Calculation - Matches symbols across lines to determine winnings.
   - Balance Management - Tracks and updates the player’s balance based on bets and winnings.
   - User Interface (CLI-based) - Uses command-line inputs for interaction.

Technical Breakdown:
   - Randomization: The slot machine outcomes are generated using random.choice().
   - Data Structures: Dictionaries store symbol counts and values; lists manage slot columns.
   - Looping & Conditionals: Used for user input validation and game logic.
   - Function Decomposition: Code is modularized with functions like deposit(), get_bet(), play_slot_machine(), etc.
   - Testing: Uses pytest for automated testing of betting, deposit, and winning calculations.

Learning Outcomes
   - Handling user input validation.
   - Working with randomized outputs in Python.
   - Understanding basic game logic and balance tracking.
   - Implementing modular programming for better code readability.
   - Writing unit tests using pytest.
   
## **Getting Started**

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.13.2 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aeriech/python-slot-machine.git
   ```

2. Install dependencies:
   ```bash
   cd python-slot-machine
   pip install pytest
   ```

3. Run development:
   ```bash
   python main.py
   ```

4. Run test:
   ```bash
   pytest test_main.py
   ```