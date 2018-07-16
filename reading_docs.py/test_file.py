from itertools import dropwhile, islice


with open("converted_pdf.txt", "r") as fin:
    start_at = dropwhile(lambda L: 'Education' not in L.split(), fin)
    for line in islice(start_at, 1, None): # ignore the line still with Abstract in
        print(line)
