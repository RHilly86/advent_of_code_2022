scoring = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3  # Scissors
}

with open("data/aoc_day2.txt") as file:
    data = file.readlines()
    strategy_guide = [line.split() for line in data]
    opponent = [line[0] for line in strategy_guide]
    your_choices = [line[1] for line in strategy_guide]
   
your_points = []
 
for player_1, player_2 in zip(opponent, your_choices):
    player_2_choice_points = scoring[player_2]
    
    if player_1 == "A":
        if player_2 == "X":
            player_2_choice_points += 3
        elif player_2 == "Y":
            player_2_choice_points += 6
            
    if player_1 == "B":
        if player_2 == "Y":
            player_2_choice_points += 3
        elif player_2 == "Z":
            player_2_choice_points += 6
    
    if player_1 == "C":
        if player_2 == "Z":
            player_2_choice_points += 3
        elif player_2 == "X":
            player_2_choice_points += 6
            
    your_points.append(player_2_choice_points)
    
print(sum(your_points))

scoring = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors,
    "X": 0, # You must lose,
    "Y": 3, # You must end in a draw
    "Z": 6  # You must win
}

your_points = []
    
for player_1, player_2 in zip(opponent, your_choices):
    if player_1 == "A":
        if player_2 == "X":
            player_2_points = scoring[player_2] + scoring["C"]
        elif player_2 == "Y":
            player_2_points = scoring[player_2] + scoring["A"]
        elif player_2 == "Z":
            player_2_points = scoring[player_2] + scoring["B"]
        
    if player_1 == "B":
        if player_2 == "X":
            player_2_points = scoring[player_2] + scoring["A"]
        elif player_2 == "Y":
            player_2_points = scoring[player_2] + scoring["B"]
        elif player_2 == "Z":
            player_2_points = scoring[player_2] + scoring["C"]
            
    if player_1 == "C":
        if player_2 == "X":
            player_2_points = scoring[player_2] + scoring["B"]
        elif player_2 == "Y":
            player_2_points = scoring[player_2] + scoring["C"]
        elif player_2 == "Z":
            player_2_points = scoring[player_2] + scoring["A"]
    
    your_points.append(player_2_points)
    
print(sum(your_points))
            
        