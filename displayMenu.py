# Function: displayMenu
# Shows menu options and returns user's selection

def displayMenu():
    print("1. Play Season")
    print("2. Quit")
    choice = input("Enter your choice: ")
    return choice

# Function: chooseTeam
# Displays a list of teams and allows the user to choose one.
# If a team is provided to remove, it will not be shown.
# Returns: The name of the selected team
def chooseTeam(teamList, removeTeam=""):
    availableTeams = []

    # Create list excluding removed team
    for team in teamList:
        if team != removeTeam:
            availableTeams.append(team)

    # Display teams as menu
    for i in range(len(availableTeams)):
        print(f"{i + 1}. {availableTeams[i]}")

    # User selects team
    choice = int(input("Choose a team: "))
    return availableTeams[choice - 1]