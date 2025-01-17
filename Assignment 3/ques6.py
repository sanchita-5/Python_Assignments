# Write a program for a matchstick game being played between the computer and a user. Your program should ensure that the computer always wins. Rules for the game are as follows:
# There are 21 matchsticks.
# The computer asks the player to pick 1,2,3, or 4 matchsticks.
# After the person pick, the computer does its picking.
# Whoever is forced to pick up the last matchstick loses the game.

matchsticks = 21
while matchsticks >= 1:
    print('Number of matchsticks available right now is',matchsticks)
    print('Your turn...')
    user = int(input('Pick up the matchstick(s)--(1-4): '))

    if user > 4:
        print('Invalid Selection')
        break

    if matchsticks == 1:
        break
        
    computer = 6 - user
    print("Computer's Turn...")
    print("Computer chooses:",computer)

    

    matchsticks = matchsticks - user - computer
    continue

    

matchsticks -= 1
print('Computer Wins')
