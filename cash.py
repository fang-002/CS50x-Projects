from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
count = 0

for coin in [25, 10, 5, 1]:
    count += cents // coin
    cents %= coin

print(count)
