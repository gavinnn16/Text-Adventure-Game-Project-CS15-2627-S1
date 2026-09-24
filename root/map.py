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
                                  /       \\
                                 v         v
                         [01. BEDROOM]   [03. POWER ROOM]

================================================================================
"""


# Map Logic
def check_map(user_choice, has_map_state):
    if user_choice == "m":
        if has_map_state:
            print(MAP_ART)
        else:
            print("\n>> You need to find the Map first!\n")
        return True
    return False