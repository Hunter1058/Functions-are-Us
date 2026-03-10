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

    homeScore = random.randint(0, 3)
    awayScore = random.randint(0, 3)

    while homeScore == awayScore:
        homeScore = random.randint(0, 3)
        awayScore = random.randint(0, 3)

    if homeScore > awayScore:
        wins = wins + 1
        results["Won Against"].append(awayTeam)
    else:
        losses = losses + 1
        results["Lost Against"].append(awayTeam)

    print(f"{homeTeam}'s score: {homeScore} - {awayTeam}'s score: {awayScore}\n")

print("Teams won against:")
for team in results["Won Against"]:
    print(f" {team}")

print("\nTeams lost against:")
for team in results["Lost Against"]:
    print(f" {team}")

print(f"\nFinal season record: {wins} - {losses}")

if wins / (wins + losses) >= 0.75:
    print("Congratulations! You qualified for the NCAA Soccer Tournament!")

elif wins / (wins + losses) >= 0.50:
    print("You had a good season.")

else:
    print("Your team needs to practice!")