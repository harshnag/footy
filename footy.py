import random

# Define the playing field
field = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

# Define the home and away teams
home_team = ["home", "home", "home", "home", "home", "home"]
away_team = ["away", "away", "away", "away", "away", "away"]

# Define the current time
time = 1

# Define the current possession
possession = 1

# Define the current player
player = 1

# Define the current direction
direction = "up"

# Define the goal score
home_score = 0
away_score = 0

# Define the computer player
computer_player = random.choice(["home", "away"])

# Start the game
while True:

    # Display the current game state
    print("Game time is now", time)
    print("The current possession is", possession)
    print("The current player is", player)
    print("The current direction is", direction)
    print("The current field is:")
    print(field)

    # Get the player's input
    if player == "human":
        command = input("What would you like to do? (up, down, left, right, shoot)")
    else:
        command = random.choice(["up", "down", "left", "right", "shoot"])

    # Check the player's input
    if command == "up":
        direction = "up"
    elif command == "down":
        direction = "down"
    elif command == "left":
        direction = "left"
    elif command == "right":
        direction = "right"
    elif command == "shoot":
        if possession == 1:
            if field[0][5] == 1:
                home_score += 1
                print("***Goal! Scored by home team in minute", time)
                field[0][5] = 0
                possession = 2
            else:
                print("The ball is out of bounds")
        else:
            if field[5][0] == 2:
                away_score += 1
                print("***Goal! Scored by away team in minute", time)
                field[5][0] = 0
                possession = 1
            else:
                print("The ball is out of bounds")

    # Move the ball
    if direction == "up":
        field[player][5] = 0
        if player == 1:
            player = 5
        else:
            player = 1
    elif direction == "down":
        field[player][0] = 0
        if player == 1:
            player = 6
        else:
            player = 2
    elif direction == "left":
        field[5][player] = 0
        if player == 1:
            player = 4
        else:
            player = 0
    elif direction == "right":
        field[0][player] = 0
        if player == 1:
            player = 3
        else:
            player = 5

    # Check if the game is over
    if time == 90:
        print("Time up!")
        print("Final score")
        print("Home:", home_score)
        print("Away:", away_score)
        break

    # Increment the time
    time += 1

    # If the player is the computer, make a random move
    if player == computer_player:
        command = random.choice(["up", "down", "left", "right", "shoot"])
