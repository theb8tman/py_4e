import re
hand = open('regex_sum_42.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    for num in stuff:
        num = int(num)
        numlist.append(num)

print(sum(numlist))
