# setting up the cafves
from random import choice

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)

print(caves)


#in this file code we will handle the list of list
caves = [
            [2,3,7],
            [5,6,12]
        ]
print(caves[0])
