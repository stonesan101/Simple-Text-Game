def retry():
    choice = input("Try Again? y/n")
    if choice == "y":
        intro(1, 1)
    else:
        print("Thank you for playing")


def easyEnding(ending, level, strength):
    print(f"You choose the easy way out.\n{ending}\nEnding Level: {level}\nEnding Strength: {strength}\nGame Over")
    retry()


def invalid(fun, level, strength):
    print("\nInvalid entry")
    fun(level, strength)


def intro(level, strength):
    print(
        f"You stand in a field.\n To the west you see a path sunny and bright.\n To the east an omnibus dark tunnel.\n")
    choice = input('Do you go east or west:')
    if choice == 'west':
        easyEnding("You go for a stroll in the woods and return home.", level, strength)
    elif choice == 'east':
        secondChoice(level, strength)
    else:
        invalid(intro, level, strength)


def secondChoice(level, strength):
    print("\nYou walk down the dark tunnel for quite a while before encountering a slime monster\nYou are unarmed\n")
    choice = input('Do you run or fight:')
    if choice == 'run':
        easyEnding('You run like a sissy back out of the tunnel', level, strength)
    elif choice == 'fight':
        thirdChoice(level, strength)
    else:
        invalid(secondChoice, level, strength)


def thirdChoice(level, strength):
    print(
        '\nYou heroically play Fisticuffs with the slime\nAfter a long fight the slime you finally defeat the slime!!\nLevel +1\n\nYou notice a chest behind the dead slime and open it.\nInside you find a Bronze Sword\nStrength +5\n')
    level += 1
    strength += 5
    choice = input('Do you continue or leave:')
    if choice == 'leave':
        easyEnding('You exit the tunnel feeling only slightly like a sissy.', level, strength)
    elif choice == 'continue':
        fourthChoice(level, strength)
    else:
        invalid(thirdChoice, level, strength)


def fourthChoice(level, strength):
    print(
        "\nYou reach the end of the tunnel and find another chest.\nJust as you touch the chest you're startled by a loud thud behind you!\nYou Turn around to find the skeleton knight 'Mr Boney Pants Guy'\nWith your exit blocked you have no choice but to fight!\nIt's a downhill battle, you're exhausted and about to faint\nYou manage to get behind the enemy, finally you have a way out\n")
    choice = input('Do you flee or fight?')
    if choice == 'flee':
        easyEnding("You barely manage to escape, you lie on the grass out of breath", level, strength)
    elif choice == 'fight':
        print(
            f"\nCRITICAL HIT!\nMr Boney Pants Guy's bones crumble to the ground\nLevel +1\nStrength +10\nEnding Level: {level+2}\nEnding Strength: {strength+10}\nThanks for playing!\n")
        retry()
    else:
        invalid(fourthChoice, level, strength)


intro(1, 1)
