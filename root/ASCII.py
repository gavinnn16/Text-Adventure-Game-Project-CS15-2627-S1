# art and other random stuff
from time import *
INSTRUCTIONS_ART = r"""
         _____ _   _  _____ _____ _____ _   _ _____ _____ _____ _   _ _____ 
        |_   _| \ | |/  ___|_   _| ___ \ | | /  __ \_   _|_   _| \ | /  ___|
          | | |  \| |\ `--.  | | | |_/ / | | | /  \/ | |   | | |  \| \ `--. 
          | | | . ` | `--. \ | | |    /| | | | |     | |   | | | . ` |`--. \
         _| |_| |\  /\__/ /  | | | |\ \| |_| | \__/\ | |  _| |_| |\  /\__/ /
         \___/\_| \_/\____/  \_/ \_| \_|\___/ \____/ \_/  \___/\_| \_/\____/ 
        """
instructions =( fr"""
print("================================================================================================")
You wake up to your AI agent, Cara, telling you that you need to escape the spaceship!
Explore the spaceship to complete these objectives:
  • Keycard
  • Turn the generator on
  • Acquire taser
  • Get samples
  • Find the escape pod key
  • Find the map to aid you (you do not need it to escape)
  • Find all code snippets

type in the numbers in brackets when you are choosing
================================================================================================
""")
def instructionstxt():
    while True:
        user_input = input("Type 'Next' when read: ").strip().lower()

        if user_input == "next":
            print("You wake up to your AI agent, Cara, telling you that you need to escape the spaceship!")
            break
        else:
            print("Invalid command. Please type 'next'.")

    while True:
        user_input = input("Type 'Next' when read: ").strip().lower()

        if user_input == "next":
            print("Explore the spaceship to complete these objectives:")
            break
        else:
            print("Invalid command. Please type 'next'.")

    while True:
        user_input = input("Type 'Next' when read: ").strip().lower()

        if user_input == "next":
            print("""Explore the spaceship to complete these objectives:
      • Keycard
      • Turn the generator on
      • Acquire taser
      • Get samples
      • Find the escape pod key
      • Find the map to aid you (you do not need it to escape)
      • Find all code snippets

      Type in the numbers in brackets when you are choosing
      ================================================================================================""")
            break
        else:
            print("Invalid command. Please type 'next'.")
