# Soccer Teams Program: asks the user to enter a home soccer team and the number of games they’ll play in a season.
# It will then ask about the teams they play against and randomly generate scores for games they play.
# It will then display information about the home team’s wins, losses, and overall performance

import random

#Prompt the user:
#Enter the name of your home team:
homeTeam = input(“Enter the name of your home team: “)

#Then, prompt the user:
#Enter the number of games that <home team name> will play:
#You can assume the user will enter a valid integer, you don’t need enter checks for invalid input.
#Tip: When first testing your code, keep the number of games low (like 2) so it is quicker to run through.
numGames = int(input(f”Enter the number of games that {homeTeam} will play: “))

wins = 0
losses = 0

#Keep track of the number of wins / losses of your home team however you want.
results = {
    “Won Against”: [],
    “Lost Against”: []
}

# Ask the name of the away team (e.g. “Utah State”) and include which number game this will be for.
#Enter the name of the away team for game <game number>:
#e.g. for the first game your team plays it should say:
#Enter the name of the away team for game 1:
for number in range(1, numGames+1):
    awayTeam = input(f”Enter the name of the away team for game {number}: “)

    #After entering in the away team name, randomly generate scores between 0 and 3 (inclusive) for the home team and the away team.
    homeScore = random.randint(0, 3)
    awayScore = random.randint(0, 3)

    while homeScore == awayScore:
        homeScore = random.randint(0, 3)
        awayScore = random.randint(0, 3)

    if homeScore > awayScore:
        wins = wins + 1
        results[“Won Against”].append(awayTeam)
    else:
        losses = losses + 1
        results[“Lost Against”].append(awayTeam)

    print(f”{homeTeam}’s score: {homeScore} - {awayTeam}’s score: {awayScore}\n”)

#After playing the game
print(“Teams won against:“)
for team in results[“Won Against”]:
    print(f” {team}“)

print(“\nTeams lost against:“)
for team in results[“Lost Against”]:
    print(f” {team}“)

#Print out Final season record followed by their record, which is the number of wins, with a dash, then the number of losses. Like this:
#Final season record: <number of wins> - <number of losses>
print(f”\nFinal season record: {wins} - {losses}“)

#After all of this, print out a final message based on the record of the home team.
#If they won at least 75% of their games, print out:
#Qualified for the NCAA Soccer Tournament!
if wins / (wins + losses) >= 0.75:
    print(“Congratulations! You qualified for the NCAA Soccer Tournament!“)

#If the team won at least 50% but less than 75% then print out:
#You had a good season.
elif wins/ (wins + losses) >= 0.50:
    print(“You had a good season.“)

#Otherwise print out:
#Your team needs to practice!
else: print(“Your team needs to practice!“)
