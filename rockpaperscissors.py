import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove.lower() == 'q':
            sys.exit() # Quit the program
        if playerMove.lower() == 'r' or playerMove.lower() == 'p' or playerMove.lower() == 's':
            break # Break out of the player input loop
        # Prompt user again to enter a valid key if they didn't
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove.lower() == 'r':
        print('ROCK versus...')
    elif playerMove.lower() == 'p':
        print('PAPER versus...')
    elif playerMove.lower() == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    # There should be 9 cases in total, but since the "tie" check accounts for 3 cases, we only have 7 possible comparisons here
    if playerMove.lower() == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove.lower() == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove.lower() == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove.lower() == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove.lower() == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove.lower() == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove.lower() == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1