from cs50 import get_string

text = get_string("Text: ")

letters = sum(1 for c in text if c.isalpha())
words = len(text.split())
sentences = sum(1 for c in text if c in ['.', '!', '?'])

L = (letters / words) * 100
S = (sentences / words) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
