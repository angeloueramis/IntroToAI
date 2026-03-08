from itertools import combinations
from collections import Counter

#example1
transactions = [
    ["Python", "Data Structures", "Algorithms"],
    ["Python", "Machine Learning"],
    ["Python", "Data Structures"],
    ["Data Structures", "Algorithms"],
    ["Python", "Algorithms"]
]

min_frequency = 2
item_counts = Counter()

for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1

frequent_items = {item for item, count in item_counts.items() if count >= min_frequency}
print("Frequent Materials:")
for item in frequent_items:
    print(item)

pair_counts = Counter()

for transaction in transactions:
    filtered = [item for item in transaction if item in frequent_items]
    for pair in combinations(filtered, 2):
        pair_counts[pair] += 1

print("\nFrequent Pairs:")
for pair, count in pair_counts.items():
    if count >= min_frequency:
        print(pair, "-> frequency:", count)



#example 2
sessions = [
    ["AI", "Python", "Machine Learning"],
    ["Python", "Data Science"],
    ["AI", "Machine Learning"],
    ["Python", "Machine Learning"],
    ["AI", "Python"]
]

min_frequency = 2
item_counts = Counter()

for session in sessions:
    for topic in session:
        item_counts[topic] += 1

print("\nFrequent Topics:")
frequent = {item for item, count in item_counts.items() if count >= min_frequency}
for item in frequent:
    print(item)

pair_counts = Counter()
for session in sessions:
    filtered = [i for i in session if i in frequent]
    for pair in combinations(filtered, 2):
        pair_counts[pair] += 1

print("\nFrequent Topic Pairs:")
for pair, count in pair_counts.items():
    if count >= min_frequency:
        print(pair, "-> frequency:", count)