# Expense Tracker
#### Video Demo: https://youtu.be/7gFvRzkx_mw
#### Description:
My final project for CS50x is a simple command-line Expense Tracker written in Python. The main goal of this project is to provide a quick and easy way for users to keep track of their daily spending directly from the terminal.

The project consists of a single file, `project.py`, which contains the main logic. The `main()` function runs a continuous loop that presents the user with a menu. Users can choose to add an expense, view their total spending, or exit the program.

When a user chooses to add an expense, they are prompted to enter the item's name and its cost. The program uses a `try/except` block to handle `ValueError`. This is an important design choice because it prevents the program from crashing if the user accidentally types letters instead of numbers when entering the cost. If the input is valid, the cost is added to a running total variable.

The "Show Total" feature simply prints the current sum of all expenses added during that session. I decided to keep the data in memory (RAM) rather than using a database or a CSV file. This was a deliberate design choice to keep the project simple, fast, and focused on core Python concepts like loops, conditionals, and error handling.

Through this project, I applied several concepts I learned in CS50. I used functions to organize my code, variables to store the total amount, and conditionals to handle the user's menu choices. I also used the `float()` function to convert the user's input into a number.

I used AI as a helper to understand the best way to structure the `try/except` block and to debug a minor syntax error.

Thank you for reviewing my project!
