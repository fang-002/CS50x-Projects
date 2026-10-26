# Expense Tracker
#### Video Demo: https://youtu.be/7gFvRzkx_mw
#### Description:
My final project for CS50x is a simple command-line Expense Tracker written entirely in Python. The primary motivation behind this project was to create a practical, easy-to-use application that solves a common everyday problem: keeping track of daily spending. Instead of relying on complex graphical interfaces or external databases, I wanted to focus on a lightweight solution that runs directly in the terminal.

The entire project is contained within a single file, `project.py`. This file contains the core logic and user interface. The `main()` function serves as the entry point of the application. It uses a continuous `while True` loop to keep the program running and to repeatedly display a menu to the user. The menu gives the user three choices: adding an expense, viewing the total expenses, or exiting the program.

One of the most important features of this project is error handling. When a user chooses to add an expense (option 1), they are prompted to enter the name of the item they bought and its cost. Because the `input()` function in Python always returns a string, I used the `float()` function to convert the user's input into a decimal number. However, if the user accidentally types a word (like "ten" instead of "10") or leaves the field blank, the `float()` function would normally raise a `ValueError` and crash the entire program. To prevent this, I implemented a `try/except` block. If a `ValueError` is caught, the program prints a friendly error message asking the user to enter a valid number, and the loop continues without crashing.

For the design choices, I deliberately decided to keep the expense data in memory (using a Python variable to store the running total) rather than saving it to a database like SQLite or a file like CSV. While saving to a file would make the data persistent across different sessions, I felt that for the scope of this Minimum Viable Product (MVP), keeping it in memory was the most efficient and straightforward approach. It allowed me to focus on mastering core Python concepts—such as loops, conditionals, functions, and exception handling—without getting bogged down by file input/output operations or SQL queries. In a future version of this project, I plan to implement file persistence using the `csv` module so that users can track their expenses over multiple days.

When the user selects option 2, the program simply prints the current total. This is calculated by adding up all the valid expenses entered during the current session. It provides immediate feedback to the user. When the user selects option 3, the program says goodbye and uses the `break` statement to exit the `while` loop, ending the program.

Through this project, I applied several concepts I learned throughout CS50x. I used functions to organize my code, variables to store the total amount, and conditionals (if/elif/else) to handle the user's menu choices. I also gained a deeper understanding of how to handle user input safely and how to prevent programs from crashing due to unexpected input.

In accordance with the course's academic honesty policy, I used AI (specifically an AI assistant) as a helper to understand the best way to structure the `try/except` block and to ensure my README file was detailed enough to meet the requirements. The core logic and the essence of the work remain entirely my own.

Thank you for reviewing my project. This was CS50!
