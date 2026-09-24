from map import *
from time import sleep
from variables import *
from ASCII import *

# intro
print("Hey, wake up we need to escape the space ship")
print(INSTRUCTIONS_ART)
print("================================================================================================")
print("""You wake up to your AI agent, Cara, telling you that you need to escape the spaceship!


Explore the spaceship to complete these objectives:
  • Keycard
  • Turn the generator on
  • Acquire taser
  • Get samples
  • Find the escape pod key
  • Find the map to aid you (you do not need it to escape)
  • Find all code snippets
""")
print("type in the numbers in brackets when you are choosing")
print("================================================================================================")

while True:
    user_input = input("Type 'Start' when ready!😀").strip().lower()
    if user_input == "start":
        break
    print("Invalid command. Please type 'Start'.")

# Main Game
while True:
    if current_room == "Bedroom":
        while True:
            print(f"Your current room is {current_room}")
            print("What would you like to do? (Go to Main Hallway(1), Search Room(2)) ")
            choice = input().strip().lower()

            if check_map(choice, has_map):
                continue


            if choice in ["1", "2"]:
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

    if current_room == "Main Hallway":
        print(f"Your current room is {current_room}")
        print("There is nothing to search in this room!")
        while True:
            print("What would you like to do? (Go to Power room(1), Med Bay(2), Bedroom(3))")
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

    if current_room == "Power Room":
        print(f"Your current room is {current_room}")
        while True:
            print("What would you like to do? (Search Room(1), Go to Main Hallway(2))")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in ["1", "2"]:
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

    if current_room == "Med Bay":
        print(f"Your current room is {current_room}")
        while True:
            print("What would you like to do? (Search Room(1), Go to Main Hallway(2), Go to Storage Room (3), Go to Central Hub (4) )")
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

    if current_room == "Storage Room":
        print(f"Your current room is {current_room}")
        while True:
            print("What would you like to do? (Search Room(1), Go to Lab(2), Go to Main hall (3))")
            choice = input().strip().lower()
            if check_map(choice, has_map):
                continue
            if choice in ["1", "2", "3"]:
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
                    current_room = "Main Hallway"
                break