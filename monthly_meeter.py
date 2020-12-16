import json
import random

members = [
    'Steven Cho',
    'Patty Gao',
    'Simon Ruiz',
    'Michelle Zhang',
    'Erika Sheng',
    'Joon Yoo',
    'Timothy Kang',
    'Ellen Shi',
    'Linda Fu',
    'Eugenia Kim',
    'Stephen Lee',
    'Nat Nah'
]

counts = {}

def build_new_counts():
    for m in members:
        if not counts.get(m):
            counts[m] = {}
        for n in members:
            if not m == n and not counts[m].get(n):
                counts[m][n] = 0
    with open('counts.json', 'w') as counts_file:
        json.dump(counts, counts_file)

def read_counts():
    with open('./counts.json') as counts_file:
        counts = json.load(counts_file)

def randomize(num, group_size):
    attempts = []
    for n in range(num):
        randomized = members.copy()
        random.shuffle(randomized)
        attempts.append(score_group([randomized[i:i + group_size] for i in range(0, len(randomized), group_size)]))
    return attempts

def score_group(groups):
    score = 0
    for group in groups:
        for person in group:
            if counts.get(person):
                for other in group:
                    if not person == other:
                        score += counts[person].get(other, 0)
    return (score, groups)

def update_counts(groups):
    for group in groups:
        for person in group:
            if not counts.get(person):
                counts[person] = {}
            for other in group:
                if not person == other:
                    if counts[person].get(other):
                        counts[person][other] += 1
                    else:
                        counts[person][other] = 1
    
    with open('counts.json', 'w') as counts_file:
        json.dump(counts, counts_file)

def pretty_print(groups):
    for group_num in range(len(groups)):
        group = groups[group_num]
        line = "Group " + str(group_num + 1) + ": "
        for person in group:
            line += person + " "
        print(line)
            

def main():
    read_counts()
    build_new_counts()
    final_group = min(randomize(5, 3), key=lambda t: t[0])
    update_counts(final_group[1])
    pretty_print(final_group[1])

if __name__ == '__main__':
    main()