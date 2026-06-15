# -----
# Name: Hanniel Nwokeji
# Course: CS 30
# Final TBG Project
# Escape the Abandoned Lab
# -----

import random

# -----
# GAME DATA
# -----

characters = {
    "lab creature": {
        "description": "A mutated experiment hunting anything alive.",
        "danger_level": "high"
    },
    "lost scientist": {
        "description": "A survivor trying to escape the lab.",
        "danger_level": "low"
    },
    "security drone": {
        "description": "An AI robot that eliminates intruders.",
        "danger_level": "medium"
    }
}

inventory = {
    "keycard": False,
    "flashlight": False,
    "power cell": False
}

player = {
    "health": 3
}

# -----
# HELPERS
# -----

def show_status():
    print("\n=== STATUS ===")
    print(f"Health: {player['health']}")
    print("Inventory:")
    for item, owned in inventory.items():
        print(f"- {item}: {'Yes' if owned else 'No'}")


def get_choice(prompt, options):
    choice = input(prompt).lower().strip()
    while choice not in options:
        print("Invalid choice.")
        choice = input(prompt).lower().strip()
    return choice


def damage(amount):
    player["health"] -= amount
    print(f"\nYou took {amount} damage! Health now: {player['health']}")


def check_death():
    if player["health"] <= 0:
        print("\n💀 You collapsed in the abandoned lab...")
        print("GAME OVER")
        return True
    return False


# -----
# MAIN GAME
# -----

def start_game():

    print("\nYou wake up inside a sealed experimental lab.")
    print("Alarms echo through the metal corridors.")

    # DECISION 1
    choice = get_choice(
        "\nSearch desk or leave room? (desk/leave): ",
        ["desk", "leave"]
    )

    if choice == "desk":
        print("\nYou found a keycard.")
        inventory["keycard"] = True

    if random.choice([True, False]):
        print("\n⚠ A loose pipe falls from above!")
        damage(1)
        if check_death():
            return

    # DECISION 2
    choice = get_choice(
        "\nGo left or right? (left/right): ",
        ["left", "right"]
    )

    if choice == "left":
        print("\nDark hallway ahead...")

        if random.choice([True, False]):
            print("A creature scratches you!")
            damage(1)
            if check_death():
                return

        choice = get_choice(
            "Investigate noise or hide? (investigate/hide): ",
            ["investigate", "hide"]
        )

        if choice == "investigate":
            print("\nYou find a flashlight.")
            inventory["flashlight"] = True
        else:
            print("\nYou avoid danger silently.")

    else:
        choice = get_choice(
            "\nUse computer or door? (computer/door): ",
            ["computer", "door"]
        )

        if choice == "computer":
            print("\nYou disable partial security systems.")
        else:
            if inventory["keycard"]:
                print("\nDoor unlocked with keycard.")
            else:
                print("\nLocked. You waste time searching.")
                damage(1)
                if check_death():
                    return

    # DRONE ENCOUNTER
    print("\nA security drone locks onto you!")

    choice = get_choice(
        "Run or hide? (run/hide): ",
        ["run", "hide"]
    )

    if choice == "run":
        print("\nYou escape, but get hit!")
        damage(1)

    else:
        if inventory["flashlight"]:
            print("\nYou blind the drone with the flashlight and escape safely.")
        else:
            print("\nYou hide poorly and take damage!")
            damage(1)

    if check_death():
        return

    # POWER DECISION 
    choice = get_choice(
        "\nGo to power room or exit? (power/exit): ",
        ["power", "exit"]
    )

    if choice == "power":
        print("\nYou restore power to the lab systems.")
        inventory["power cell"] = True

        if inventory["flashlight"]:
            print("The restored lights help you navigate safely.")
        else:
            print("Without a flashlight, shadows make movement harder.")
            damage(1)
            if check_death():
                return

    else:
        print("\nExit blocked. You are forced deeper into the lab.")

    # FINAL CHAMBER
    print("\nYou reach the final chamber...")
    show_status()

    choice = get_choice(
        "\nEscape or expose the lab? (escape/expose): ",
        ["escape", "expose"]
    )

    # ENDINGS 
    if choice == "escape":

        if inventory["keycard"] and inventory["power cell"] and inventory["flashlight"]:
            print("\n🏆 PERFECT ESCAPE: You navigate the lab and escape flawlessly!")
        elif inventory["keycard"] and inventory["power cell"]:
            print("\n⚠ You escape, but it was a dangerous route.")
        elif inventory["keycard"]:
            print("\n⚠ You escape using the keycard, but barely survive.")
        else:
            print("\n💀 You reach the exit... but it's locked forever.")

    else:
        print("\n🔥 You expose the lab experiments to the world.")
        print("Truth comes at a cost.")


# -----
# MENU LOOP
# -----

playing = True

while playing:

    print("\n=== ESCAPE THE ABANDONED LAB ===")
    print("1. Start Game")
    print("2. View Status")
    print("3. Help")
    print("4. Quit")

    choice = input("\nChoose an option (1-4): ").strip()

    if choice == "1":
        start_game()

    elif choice == "2":
        show_status()
        input("\nPress Enter...")

    elif choice == "3":
        print("\nExplore, survive, and escape the lab.")
        input("\nPress Enter...")

    elif choice == "4":
        print("\nThanks for playing!")
        playing = False

    else:
        print("\nInvalid input.")