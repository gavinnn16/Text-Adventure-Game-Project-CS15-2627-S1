# Map
MAP_ART = """
================================================================================

                           [10. ESCAPE PODS] (WIN)
                                      ^
                                      |
                               [09. AIRLOCK]
                                      ^
                                      |
        +-----------------------------+-----------------------------+
        |                             |                             |
  [07. LAB] <---------> [05. CENTRAL HUB] <---------> [08. SECURITY ROOM]
        ^                             |
        |                             v
  [06. STORAGE] <------------ [04. MED BAY]
                                      |
                                      v
                             [02. MAIN HALLWAY]
                                  /       \
                                 v         v
                         [01. BEDROOM]   [03. POWER ROOM]

================================================================================
"""


# Map Logic
def check_map(user_choice: str, has_map_state: bool) -> bool:
    """Check if the user wants to view the map and if they have the map.

    :param user_choice: The user's input choice.
    :param has_map_state: Whether the user has the map or not.
    :return: True if map command was handled, False otherwise.
    """
    if user_choice == "m":
        if has_map_state:
            print(MAP_ART)
        else:
            print("\n>> You need to find the Map first!\n")
        return True
    return False

