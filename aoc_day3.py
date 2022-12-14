priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

item_type_priorities = []

with open("data/aoc_day3.txt") as file:
    data = file.read().splitlines()
    for line in data:
        midpoint = len(line) // 2
        first_compartment = set(line[:midpoint])
        second_compartment = set(line[midpoint:])
        intersection = list(first_compartment.intersection(second_compartment))[0]
        item_type_priorities.append(priority[intersection])
        
print(sum(item_type_priorities))

item_type_priorities = []

with open("data/aoc_day3.txt") as file:
    data = file.read().splitlines()
    for index in range(0, len(data), 3):
        group = data[index:index+3]
        intersection = list(set(group[0]).intersection(*group))[0]
        item_type_priorities.append(priority[intersection])
        
print(sum(item_type_priorities))