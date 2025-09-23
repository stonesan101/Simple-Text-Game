def retry():
    choice = input("Try Again? y/n: ")
    # restart game
    if choice.lower() == "y":
        partOne(1, 1)
    # end game
    else:
        print("\nThank you for playing!")


# 3c
def inputLoop(inputText, endingText, continueInput, endingInput, nextFun, level, strength):
    # 2b
    while (True):
        choice = input(inputText).lower()
        # run next function
        if choice == continueInput:
            nextFun(level, strength)
            # 2c
            break
        # early ending
        if choice == endingInput:
            print(
                f"You choose the easy way out.\n{endingText}\nEnding Level: {level}\nEnding Strength: {strength}\nGame Over")
            retry()
            break
        # invalid input
        else:
            print(f"\nInvalid Input\nPlease choose {continueInput} or {endingInput}\n")
            # 2d
            continue


# 3f
def partOne(level=1, strength=1):
    printStars()

    print(
        f"You stand in a field.\n To the west you see a path sunny and bright.\n To the east an omnibus dark tunnel.\n")

    inputText = 'Do you go east or west:'
    endingText = "You go for a stroll in the woods and return home."
    continueInput = 'east'
    endingInput = 'west'
    inputLoop(inputText, endingText, continueInput, endingInput, partTwo, level, strength)


def partTwo(level, strength):
    print("\nYou walk down the dark tunnel for quite a while before encountering a slime monster\nYou are unarmed\n")

    inputText = 'Do you run or fight: '
    endingText = 'You run like a sissy back out of the tunnel'
    continueInput = 'fight'
    endingInput = 'run'
    inputLoop(inputText, endingText, continueInput, endingInput, partThree, level, strength)


def partThree(level, strength):
    print(
        '\nYou heroically play Fisticuffs with the slime\nAfter a long fight the slime you finally defeat the slime!!\nLevel +1\n\nYou notice a chest behind the dead slime and open it.\nInside you find a Bronze Sword\nStrength +5\n')

    level += 1
    strength += 5

    inputText = 'Do you continue or leave: '
    endingText = 'You exit the tunnel feeling only slightly like a sissy.'
    continueInput = 'continue'
    endingInput = 'leave'
    inputLoop(inputText, endingText, continueInput, endingInput, partFour, level, strength)


def partFour(level, strength):
    print(
        "\nYou reach the end of the tunnel and find another chest.\nJust as you touch the chest you're startled by a loud thud behind you!\nYou Turn around to find the skeleton knight 'Mr Boney Pants Guy'\nWith your exit blocked you have no choice but to fight!\nIt's a downhill battle, you're exhausted and about to faint\nYou manage to get behind the enemy, finally you have a way out\n")

    inputText = 'Do you flee or fight: '
    endingText = "You barely manage to escape, you lie on the grass out of breath"
    continueInput = 'fight'
    endingInput = 'flee'
    inputLoop(inputText, endingText, continueInput, endingInput, partFive, level, strength)


def partFive(level, strength):
    print(
        f"\nCRITICAL HIT!\nMr Boney Pants Guy's bones crumble to the ground\nLevel +2\nStrength +10\n\nEnding Level: {level+2}\nEnding Strength: {strength+10}\nThanks for playing!")

    choice = input("Try Again? y/n: ")
    if choice.lower() == "y":
        partOne()
    else:
        print("\nThank you for playing!")


# 3a
def printStars():
    # 2a
    for i in range(2):
        # 2e
        for j in range(40):
            print("*", end=" ")
        print()


partOne()

# recursive version of inputLoop
def recursiveLoop(inputText, endingText, continueInput, endingInput, nextFun, level, strength):
    choice = input(inputText).lower()
    if choice == continueInput:
        nextFun(level, strength)
    if choice == endingInput:
        print(
            f"You choose the easy way out.\n{endingText}\nEnding Level: {level}\nEnding Strength: {strength}\nGame Over")
        retry()

    else:
        print(f"\nInvalid Input\nPlease choose {continueInput} or {endingInput}\n")
        # 4b
        recursiveLoop(inputText, endingText, continueInput, endingInput, nextFun, level, strength)
