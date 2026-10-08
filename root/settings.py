# art and other random stuff
from time import *
INSTRUCTIONS_ART = r"""
┌─────────────────────────────────┐
│     I N S T R U C T I O N S     │
└─────────────────────────────────┘
"""
def instructionstxt() -> None:
    """Displays sequential introductory story and objectives to the player."""
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
            print("""
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



