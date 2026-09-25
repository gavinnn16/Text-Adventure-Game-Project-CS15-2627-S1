from map import *
from variables import *
from ASCII import *
from time import *

# intro
print(INSTRUCTIONS_ART)
print(instructionstxt())
while True:
    user_input = input("Type 'Start' when ready!😀").strip().lower()
    if user_input == "start":
        break
    print("Invalid command. Please type 'Start'.")

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
            if choice in ["1", "2",]:
                if choice == "1":
                    current_room = "Hallway to Airlock"

                if choice == "2":
                    if not has_keycard:
                        print("Searching")
                        sleep(0.5)
                        print(".")
                        sleep(0.5)
                        print(".")
                        sleep(0.5)
                        print(".")
                        print("You found somthing!")
                        sleep(1)
                        print("Its a keycard💳")
                        sleep(1)
                        print("Use it in the Power Room to unlock all the doors in the ship!")
                        has_keycard = True
                    else:
                        print("you already have the keycard")
                break
# Main Hallway
    if current_room == "Main Hallway":
        print(f"Your current room is {current_room} You look around and see a few doors to other rooms, decoration, looks like there used to be a lot of people here but now it looks abandoned")
        print("Unfortunately There is nothing to search in this room!")
        while True:
            print("""What would you like to do? 
1. Go to Power room
2. Med Bay 
3. Bedroom""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in ["1", "2", "3"]:
                if choice == "1":
                    current_room = "Power Room"
                elif choice == "2":
                    if generator_powered:
                        print("The door lifts open")
                        current_room = "Med Bay"
                    else:
                        print("You need to unlock this door from the power room!")
                elif choice == "3":
                    current_room = "Bedroom"
                break
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
            if choice in ["1", "2",]:
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
                        print("You found somthing")
                        sleep(1)
                        print("It looks like the generator needs authentication find a keycard! ")
                    else:
                        generator_powered = True
                        print("You have powered the generator! look around and see what you can find!")

                elif choice == "2":
                    current_room = "Main Hallway"
                break
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
            if choice in ["1", "2", "3", "4"]:
                if choice == "1":
                    print("working")
                elif choice == "2":
                    current_room = "Main Hallway"
                elif choice == "3":
                    current_room = "Storage Room"
                else:
                    current_room = "Central Hub"
                break
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
                if choice in ["1", "2", "3"]:
                    if choice == "1":
                        print("Searching")
                        sleep(0.5)
                        print(".")
                        sleep(0.5)
                        print(".")
                        sleep(0.5)
                        print(".")
                        sleep(1)
                        print("You found somthing")
                        sleep(1)
                        print("It looks like you found a Map to the ship!")
                        print("From now on you can type 'M' at any prompt to open the map!")
                    elif choice == "2":
                        current_room = "Lab"
                    elif choice == "3":
                        current_room = "Med Bay"
                    break
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
            if choice in ["1", "2", "3", "4", "5"]:
                if choice == "1":
                    print("Searching")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(1)
                    print("You found somthing")
                    sleep(1)
                    print("It looks like you found a code snippet for the escape pod!")
                    sleep(1)
                    print("The code snippet is 5")
                elif choice == "2":
                    current_room = "Security Room"
                elif choice == "3":
                    current_room = "Lab"
                elif choice == "4":
                    current_room = "Hallway to Airlock"
                else:
                    current_room = "Med Bay"
                break
#Security Room
    if current_room == "Security Room":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1. Search Room
2. Go to Central Hub""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in ["1", "2",]:
                if choice == "1":
                    print("Searching")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(1)
                    print("You found somthing")
                    sleep(1)
                    print("It looks like you found a taser, I wonder what you would need it for 👽")
                    has_taser = True
                else:
                    current_room = "Central Hub"
                break
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
            if choice in ["1", "2", "3"]:
                if choice == "1":
                    print("Searching")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(0.5)
                    print(".")
                    sleep(1)
                    print("You found somthing")
                    sleep(1)
                    print("It looks like you found a Sample, keep it safe 🧪")
                    has_samples = True
                elif choice == "2":
                    current_room = "Storage Room"
                else:
                    current_room = "Med Bay"
                break


    if current_room == "Hallway to Airlock":
            print(f"Your current room is %#(@&%^@*$(@&$")
            sleep(1)
            print("""
You see the Airlock door however its there is an screen that says 'Administrator has locked the door'
It looks like you need a overide code, you need to find it and enter it.
            """)
            while True:
                print("""What would you like to do?
    1. Enter Code
    2. Go to Central Hub""")
                choice = input().strip().lower()
                if check_map(choice, has_map):
                    continue
                if choice in ["1", "2"]:
                    if choice == "1":
                        user_code = input("Enter the override code: ").strip()
                        if user_code == "5921":
                            print("Code accepted! The Airlock door opens!")
                            current_room = "Airlock"
                        else:
                            print("Incorrect code. The door remains locked.")
                    elif choice == "2":
                        current_room = "Central Hub"
                    break



if current_room == "Airlock":
                    print("You escaped the spaceship! YOU WIN!")
                    end_time = monotonic()
                    elapsed_time = end_time - start_time
                    elapsed_time = round(elapsed_time, 2)

                    print(f"Total time played: {elapsed_time} seconds")








