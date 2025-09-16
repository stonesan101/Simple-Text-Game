def retry():
    choice = input("Try Again? y/n: ")
    if choice.lower() == "y":
        intro(1, 1)
    else:
        print("\nThank you for playing!")


def easyEnding(ending, level, strength):
    print(f"You choose the easy way out.\n{ending}\nEnding Level: {level}\nEnding Strength: {strength}\nGame Over")
    retry()


def whileLoop(inputText, endingText, continueInput, endingInput, nextFun, level, strength):
    while (True):
        choice = input(inputText).lower()
        if choice == continueInput:
            nextFun(level, strength)
            break
        if choice == endingInput:
            easyEnding(endingText, level, strength)
            break
        else:
            print(f"\nInvalid Input\nPlease choose {continueInput} or {endingInput}\n")


def invalid(fun, level, strength):
    print("\nInvalid entry")
    fun(level, strength)


def intro(level, strength):
    print(
        f"You stand in a field.\n To the west you see a path sunny and bright.\n To the east an omnibus dark tunnel.\n")
    inputText = 'Do you go east or west: '
    endingText = "You go for a stroll in the woods and return home."
    continueInput = 'east'
    endingInput = 'west'
    whileLoop(inputText, endingText, continueInput, endingInput, secondChoice, level, strength)


def secondChoice(level, strength):
    print("\nYou walk down the dark tunnel for quite a while before encountering a slime monster\nYou are unarmed\n")
    inputText = 'Do you run or fight: '
    endingText = 'You run like a sissy back out of the tunnel'
    continueInput = 'fight'
    endingInput = 'run'
    whileLoop(inputText, endingText, continueInput, endingInput, thirdChoice, level, strength)


def thirdChoice(level, strength):
    print(
        '\nYou heroically play Fisticuffs with the slime\nAfter a long fight the slime you finally defeat the slime!!\nLevel +1\n\nYou notice a chest behind the dead slime and open it.\nInside you find a Bronze Sword\nStrength +5\n')
    level += 1
    strength += 5
    inputText = 'Do you continue or leave: '
    endingText = 'You exit the tunnel feeling only slightly like a sissy.'
    continueInput = 'continue'
    endingInput = 'leave'
    whileLoop(inputText, endingText, continueInput, endingInput, fourthChoice, level, strength)


def fourthChoice(level, strength):
    print(
        "\nYou reach the end of the tunnel and find another chest.\nJust as you touch the chest you're startled by a loud thud behind you!\nYou Turn around to find the skeleton knight 'Mr Boney Pants Guy'\nWith your exit blocked you have no choice but to fight!\nIt's a downhill battle, you're exhausted and about to faint\nYou manage to get behind the enemy, finally you have a way out\n")
    inputText = 'Do you flee or fight?'
    endingText = "You barely manage to escape, you lie on the grass out of breath"
    continueInput = 'fight'
    endingInput = 'flee'
    whileLoop(inputText, endingText, continueInput, endingInput, finalEnding, level, strength)


def finalEnding():
    choice = input("Try Again? y/n: ")
    if choice.lower() == "y":
        intro(1, 1)
    else:
        print("\nThank you for playing!")


intro(1, 1)
