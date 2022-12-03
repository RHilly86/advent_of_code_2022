# We want to find the Elf carrying the most amount of calories

# Open the file and split the data on two new lines
with open('data/aoc_day1_part1.txt') as f:
    data = f.read().split('\n\n')
    lines = [line.split() for line in data]
    max_calories = max(sum([int(x) for x in line]) for line in lines)
    print(max_calories)
    
with open("data/aoc_day1_part1.txt") as f:
    data = f.read().split("\n\n")
    lines = [line.split() for line in data]
    calories = [sum([int(x) for x in line]) for line in lines]
    top_three = sorted(calories, reverse=True)[:3]
    print(sum(top_three))