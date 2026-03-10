# Hunter Potter, Erik Peterson, 
# Eugene Son, Penina Strong;

# Soccer Teams Program: asks the user to enter a home soccer team and the number of games they’ll play in a season.
# It will then ask about the teams they play against and randomly generate scores for games they play.
# It will then display information about the home team’s wins, losses, and overall performance

from Functions import play_game, displayMenu, chooseTeam, final_season_record
import random

# Prompt the user
homeTeam = input("Enter the name of your home team: ")

numGames = int(input(f"Enter the number of games that {homeTeam} will play: "))

wins = 0
losses = 0

results = {
    "Won Against": [],
    "Lost Against": []
}

for number in range(1, numGames + 1):
    awayTeam = input(f"Enter the name of the away team for game {number}: ")

    result = play_game(homeTeam, awayTeam)  # <-- replaces all the score generation code

    if result == 'W':
        wins += 1
        results["Won Against"].append(awayTeam)
    else:
        losses += 1
        results["Lost Against"].append(awayTeam)

print("Teams won against:")
for team in results["Won Against"]:
    print(f" {team}")

print("\nTeams lost against:")
for team in results["Lost Against"]:
    print(f" {team}")

final_season_record(wins, losses)