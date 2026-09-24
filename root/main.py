from map import *
from time import sleep
from variables import *
from ASCII import *
from choice import *

# intro
print("Hey, wake up we need to escape the space ship")
print(INSTRUCTIONS_ART)
print(instructions)
while True:
    user_input = input("Type 'Start' when ready!😀").strip().lower()
    if user_input == "start":
        break
    print("Invalid command. Please type 'Start'.")

# Starting
while True:
    if current_room == "Bedroom":
        while True:
            print(f"Your current room is {current_room}")
            print("""What would you like to do?
1 Go to Main Hallway
2 Search Room""")
            choice = input().strip().lower()

            if check_map(choice, has_map):
                continue


            if choice in cl1:
                if choice == "1":
                    current_room = "Main Hallway"
                    break
                elif choice == "2":
                    if not has_keycard:
                        print("Searching Room")
                        sleep(1)
                        print("You found somthing!")
                        sleep(1)
                        print("Its the keycard💳")
                        print("Use it in the Power Room to unlock all the doors in the ship!")
                        has_keycard = True
                    else:
                        print("you already have the keycard")
                    break
# Main Hallway
    if current_room == "Main Hallway":
        print(f"Your current room is {current_room}")
        print("There is nothing to search in this room!")
        while True:
            print("""What would you like to do? 
1 Go to Power room
2 Med Bay 
3 Bedroom""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in cl2:
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
            print("What would you like to do? (Search Room(1), Go to Main Hallway(2))")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in cl3:
                if choice == "1":
                    if not has_keycard:
                        print("Searching Room")
                        print("You found somthing")
                        print("It looks like the generator needs authentication find a keycard! ")
                    else:
                        generator_powered = True
                        print("you have powered the generator! look around and see what you can find!")

                elif choice == "2":
                    current_room = "Main Hallway"
                break
# Med Bay
    if current_room == "Med Bay":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1 Search Room
2 Go to Main Hallway
3 Go to Storage Room
4 Go to Central Hub""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in cl4:
                if choice == "1":
                    print("working")
                elif choice == "2":
                    current_room = "Main Hallway"
                elif choice == "3":
                    current_room = "Storage Room"
                else:
                    current_room = "Central Hub"
                break
# Central Hub
    if current_room == "Central Hub":
        print(f"Your current room is {current_room}")
        while True:
            print("""What would you like to do? 
1 Search Room
2 Go to Security Room
3 Go to Lab
4 Go to Airlock
5 Go to Med Bay)""")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in cl5:
                if choice == "1":
                    print("searching")
                    sleep(1)
                    print("You found somthing")
                    sleep(1)
                    print("It looks like you found a code snippet for the escape pod!")
                    print("The code snippet is 5")
                elif choice == "2":
                    current_room = "Security Room"
                elif choice == "3":
                    current_room = "Lab"
                elif choice == "4":
                    current_room = "Airlock"
                else:
                    current_room = "Med Bay"
                break
#Storage Room
    if current_room == "Storage Room":
        print(f"Your current room is {current_room}")
        while True:
            print("What would you like to do? (Search Room(1), Go to Lab(2), Go to Med Bay (3))")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in cl6:
                if choice == "1":
                        print("Searching Room")
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
