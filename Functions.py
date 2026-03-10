# Functions page
import random

# Play_game Function Recieves both team names generates no tie scores
def play_game(home_team, away_team):
    home_score = random.randint(0, 3)
    away_score = random.randint(0, 3)
    while home_score == away_score:
        home_score = random.randint(0, 3)
        away_score = random.randint(0, 3)

    print(f"\n  {home_team}'s score: {home_score}  |  {away_team}'s score: {away_score}")

    if home_score > away_score:
        print(f"  Result: {home_team} WINS!\n")
        return 'W'
    else:
        print(f"  Result: {away_team} wins. Better luck next time.\n")
        return 'L'
