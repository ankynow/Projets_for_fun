import random
#step 1 what is object "dice" -->Think how it works ?????

def roll():         #define a function for dice 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)      # to generate a random numbers

    return roll               #every time it will retun a number


#value = roll()
#print(value)

#step 2 now we need playes 

while True:
    players = input("Enter the number of players (2 - 4): ")    # input number of players
    if players.isdigit():                          #it is checking players is digit or not
        players = int(players)                     #converting the input "string" into int
        if 2 <= players <= 4:                      # max number of playes
            break                                  # to break the loop
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
#print(players)----> to print the input vale given by user 

#step 3
#ask playes to roll the dice
#list comprehension  ---->[expression for item in iterable] & [expression for item in iterable if condition]
#example: squares = [x**2 for x in range(10)]
#print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#evens = [x for x in range(10) if x % 2 == 0]
#print(evens)  # Output: [0, 2, 4, 6, 8]

#words = ["hello", "world", "python"]
#uppercase_words = [word.upper() for word in words]
#print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

#matrix = [[j for j in range(3)] for i in range(3)]
#print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)