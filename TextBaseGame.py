def Play_again():
    print('\n Do you want to play again? y/n')
    answer = input('>').lower()
    if answer == 'y':
        start()
    else:
        exit()

def game_over(reason):
    print('\n '+ reason)
    print('Game is over!!')
    Play_again()

def diamond_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead, call game_over() function with the "reason"
        game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
    elif answer == "2":
        # the player won the game
        print("\nNice, you're are an honest man! Congrats you win the game!")
        # activate play_again() function
        Play_again()
    else:
        # call game_over() with "reason"
        game_over("Go and learn how to type a number.")


def bear_room():
    print('\n You are in Bear room.')
    print('Behind the bear, there is an other door!')
    print('The bear is eating tasty honey..')
    print('What would you do? (1 or 2)')
    print('1: Take away the honey!!')
    print('2: Taunt the Bear...')

    answer =  input('>')
    if '1' in answer:
        game_over('The Bear Killed you!!')
    elif '2' in answer:
        print("\nYour Good time, the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
        game_over('You did not press the correct key!!')



def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")


    answer =  input('>')
    if '1' in answer:
        print("\nYour Good time, the monster have not woke up. You can go through it now!")
        diamond_room()

    elif '2' in answer:
        game_over('The monster Killed you!!')


    else:
        game_over('You did not press the correct key!!')


def start():
    print('\n You are standing in a dark room.')
    print('There is a door to your left or right. Which one do you take? (l or r)')

    answer = input('>').lower()
    if 'l' in answer:
        bear_room()

    elif 'r' in answer:
        monster_room()
    else:
        game_over('You did not press the correct key!!')

start()