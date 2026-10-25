import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        database = list(reader)

    with open(sys.argv[2]) as file:
        sequence = file.read()

    subsequences = list(database[0].keys())[1:]

    counts = {}
    for sub in subsequences:
        counts[sub] = longest_match(sequence, sub)

    for person in database:
        match = True
        for sub in subsequences:
            if int(person[sub]) != counts[sub]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    longes = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * sub_len
            end = start + sub_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        if count > longes:
            longes = count

    return longes


if __name__ == "__main__":
    main()
    