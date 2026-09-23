import random
from asyncio import wait
from time import sleep

from variables import *
from ASCII import *

while True:
    if current_room == "Bedroom":
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
        print("================================================================================================")


        while True:
            user_input = input("Type 'Start' when ready!😀").strip().lower()
            if user_input == "start":
                break
            print("Invalid command. Please type 'Start'.")

        while True:
            print(f"Your current room is {current_room}")
            print("Where would you like to do? (Go to Main Hallway, Search Room) ")
            choice = input().strip().lower()
            if choice in ["main hallway, search room"]:
                if choice == "main hallway":
                    current_room = "Main Hallway"
                break
            elif choice == "search room":
                print("Searching Room")
                sleep(1)
                print("Nothing found😭")


    elif current_room == "Main Hallway":
        print("Welcome to the Hallway, there is nothing in this room!")
        while True:
            print("How are you feeling?")
            choice = input().strip().lower()
            if choice in ["hungry", "full", "tired"]:
                if choice == "hungry":
                    current_room = "eating"
                elif choice == "full":
                    current_room = "coding"
                else:
                    current_room = "sleeping"
                break




