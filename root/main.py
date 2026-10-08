from map import *
from variables import *
from settings import *
from time import *
# intro
print(INSTRUCTIONS_ART)
instructionstxt()
while True:
    user_input = input("Type 'Start' when ready!😀").strip().lower()
    if user_input == "start":
        break
    print("Invalid command. Please type 'Start'.")

def invalid_response():
    """Simple function that prints an invalid response message"""
    print("❌ Invalid response, please pick a correct number. ❌")

# Starting
start_time = monotonic()

while True:
    if current_room == "Bedroom":
        while True:
            print(f"Your current room is {current_room} you get up from your blue bed and look confused")
            print("""What would you like to do?
1. Go to Main Hallway


2. Search Room""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                current_room = "Main Hallway"
                break
            elif choice == "test":

                current_room = "Hallway to Airlock"
                generator_powered = True
                med_bay_unlocked = "Unlocked"
                alien_distracted = True
                game_won = False

                # Parts for code (All 4 snippets acquired)
                has_code_snippet_1 = True  # 5
                has_code_snippet_2 = True  # 9
                has_code_snippet_3 = True  # 2
                has_code_snippet_4 = True  # 1

                # Items (All key items acquired)
                knows_override_code = True
                has_taser = True
                has_samples = True
                has_keycard = True
                has_escape_pod_key = True
                has_map = True
                break
            elif choice == "2":
                if not has_keycard:
                    print("Searching")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    print("You found something!")
                    sleep(1)
                    print("Its a keycard💳")
                    sleep(1)
                    print("Use it in the Power Room to unlock all the doors in the ship!")
                    has_keycard = True
                else:
                    print("You already have the keycard")
                break
            else:
                invalid_response()

# Main Hallway
    if current_room == "Main Hallway":
        print(f"Your current room is {current_room} You look around and see a few doors to other rooms, decoration, looks like there used to be a lot of people here but now it looks abandoned")
        print("Unfortunately There is nothing to search in this room!")
        while True:
            print(f"""What would you like to do? 
1. Go to Power room


2. Med Bay ({med_bay_unlocked}) 

3. Bedroom""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                current_room = "Power Room"
                break
            elif choice == "2":
                if generator_powered:
                    print("The door lifts open")
                    current_room = "Med Bay"
                    break
                else:
                    print("You need to unlock this door from the power room!")
            elif choice == "3":
                current_room = "Bedroom"
                break
            else:
                invalid_response()

# Power Room
    if current_room == "Power Room":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1. Search Room


2. Go to Main Hallway""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                if not has_keycard:
                    print("Searching")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(1)
                    print("You found something")
                    sleep(1)
                    print("It looks like the generator needs authentication find a keycard! ")
                else:
                    generator_powered = True
                    print("You have powered the generator! look around and see what you can find!")
                    med_bay_unlocked = "Unlocked"
                break
            elif choice == "2":
                current_room = "Main Hallway"
                break
            else:
                invalid_response()

# Med Bay
    if current_room == "Med Bay":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1. Search Room


2. Go to Main Hallway

3. Go to Storage Room

4. Go to Central Hub""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                print("Searching")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(1)
                print("You found something")
                sleep(1)
                print("It looks like its a key for something, you keep it wondering what it could be used for ")
                has_escape_pod_key = True
                break
            elif choice == "2":
                current_room = "Main Hallway"
                break
            elif choice == "3":
                current_room = "Storage Room"
                break
            elif choice == "4":
                current_room = "Central Hub"
                break
            else:
                invalid_response()

# Storage Room
    if current_room == "Storage Room":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do
1. Search Room


2. Go to Lab

3. Go to Med Bay""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                print("Searching")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(1)
                print("You found something")
                sleep(1)
                print("It looks like you found a Map to the ship!")
                print("From now on you can type 'M' at any prompt to open the map!")
                print("Under the map you saw a code snippet it looks like it says 2")
                has_code_snippet_3 = True
                has_map = True
                break
            elif choice == "2":
                current_room = "Lab"
                break
            elif choice == "3":
                current_room = "Med Bay"
                break
            else:
                invalid_response()

# Central Hub
    if current_room == "Central Hub":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1. Search Room


2. Go to Security Room

3. Go to Lab

4. Go to Airlock

5. Go to Med Bay""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                print("Searching")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(1)
                print("You found something")
                sleep(1)
                print("It looks like you found a code snippet for the escape pod!")
                sleep(1)
                print("The code snippet is 5")
                has_code_snippet_1 = True
                break
            elif choice == "2":
                current_room = "Security Room"
                break
            elif choice == "3":
                current_room = "Lab"
                break
            elif choice == "4":
                current_room = "Hallway to Airlock"
                break
            elif choice == "5":
                current_room = "Med Bay"
                break
            else:
                invalid_response()

# Security Room
    if current_room == "Security Room":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1. Search Room


2. Go to Central Hub""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                print("Searching")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(1)
                print("You found something")
                sleep(1)
                print("It looks like you found a taser, I wonder what you would need it for 👽")
                has_taser = True
                print("Woah what is this? you found a code snippet for the escape pod!")
                sleep(1)
                print("The code snippet is 9")
                has_code_snippet_2 = True
                break
            elif choice == "2":
                current_room = "Central Hub"
                break
            else:
                invalid_response()

# Lab
    if current_room == "Lab":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do?
1. Search Room


2. Go to Storage Room

3. Go to Med Bay""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                print("Searching")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(0.5)
                print(".")
                sleep(1)
                print("You found something")
                sleep(1)
                print("It looks like you found a Sample, keep it safe 🧪")
                has_samples = True
                print("While exiting you found another code sample, looks like it says 1")
                has_code_snippet_4 = True
                break
            elif choice == "2":
                current_room = "Storage Room"
                break
            elif choice == "3":
                current_room = "Med Bay"
                break
            else:
                invalid_response()

# Hall Way to Airlock
    if current_room == "Hallway to Airlock":
        print(f"Your current room is %#(@&%^@*$(@&$")
        sleep(1)
        print("""
You see the Airlock door however its there is an screen that says 'Administrator has locked the door'
It looks like you need a override code, you need to find it and enter it.
        """)
        while True:
            print("""What would you like to do?
1. Enter Code


2. Go to Central Hub""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue

            if choice == "1":
                user_code = input("Enter the override code: ").strip()
                if has_code_snippet_1 == True and has_code_snippet_2 == True and has_code_snippet_3 == True and has_code_snippet_4 == True:
                    if user_code == "5921":
                        print("Code accepted! The Airlock door opens!")
                        current_room = "Airlock"
                        break
                    else:
                        print("Incorrect code. The door remains locked.")
                else:
                    print("You don't have all the code snippets yet. Find them first!")
            elif choice == "2":
                current_room = "Central Hub"
                break
            else:
                invalid_response()


# Airlock
    if current_room == "Airlock":
        print(f"Your current room is {current_room}")
        sleep(1)

        if has_taser == False:
            print("""You're in the Airlock... an alien is blocking the escape pods. You need to find a taser!""")
            while True:
                print("""What would you like to do?
    1. Go to Central Hub""")
                choice = input().strip().lower()
                if check_map(choice, has_map):
                    continue

                if choice == "1":
                    current_room = "Central Hub"
                    break
                else:
                    invalid_response()

        else:
            while True:
                print("""What would you like to do?
    1. Tase the alien
    2. Go to Central Hub""")
                choice = input().strip().lower()
                if check_map(choice, has_map):
                    continue

                if choice == "1":
                    print("Nice job! You tased the alien and can now escape!")
                    current_room = "EscapePods"
                    break
                elif choice == "2":
                    current_room = "Central Hub"
                    break
                else:
                    invalid_response()
# Escape Pods
    if current_room == "EscapePods":
        print(f"Your current room is {current_room}")
        sleep(1)
        if has_keycard == True and has_samples == True and has_escape_pod_key == True:
            print("""
    Finally its over, your in the escape pods, you think about your adventure and wonder what happened when you were asleep.
        """)
            while True:
                print("""What would you like to do?
 1. Escape
 2. Go to Central Hub""")
                choice = input().strip().lower()
                if check_map(choice, has_map):
                    continue

                if choice == "1":

                    print("Nice job you tased the alien, it is now distracted and you can escape!")
                    current_room = "Win"
                    break
                elif choice == "2":
                    current_room = "Central Hub"
                    break
                else:
                    print("You don't have a taser to tase the alien.")
                    invalid_response()

        else:
            print(f""" Hmm looks like your missing something!""")

            if not has_keycard:
                print("- How did you even power the ship on? Well whatever, you need the keycard anyway.")
            if not has_samples:
                print(
                    "- Are you even interested in playing the game? Explore the ship man, go to the Lab and find the samples to bring back to Earth! 😒")
            if not has_escape_pod_key:
                print("- Hmmm, you forgot to search Med Bay! It has the key to escape, FIND IT!")

            while True:
                print("""What would you like to do?
             1. Go to Central Hub""")
                choice = input().strip().lower()
                if check_map(choice, has_map):
                    continue

                if choice == "1":
                    current_room = "Central Hub"
                    break
                else:
                    invalid_response()


    # Win checker
    if current_room == "Win":
        print("You escaped the spaceship! YOU WIN!")
        end_time = monotonic()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time, 2)
        print(f"Total time played: {elapsed_time} seconds")
        break