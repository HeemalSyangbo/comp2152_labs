import random


def roll_weapon():
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

    try:
        weaponRoll = random.randint(1, 6)  # Roll a dice (1-6)
        hero_combat_strength = weaponRoll  # Add roll to hero's combat strength

        weapon = weapons[weaponRoll - 1]  # Get the weapon from the array
        print(f"You rolled a {weaponRoll}. Your weapon is: {weapon}")

        # Determine weapon strength message
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll <= 4:
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend!")

        # Check if the weapon is not a Fist
        if weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


# Run the function
roll_weapon()
