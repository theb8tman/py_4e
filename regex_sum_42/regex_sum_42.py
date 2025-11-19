import re
hand = open('Unconfirmed 410553.crdownload')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    for num in stuff:
        num = int(num)
        numlist.append(num)

print(sum(numlist))
