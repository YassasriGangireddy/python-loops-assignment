# game_score.py

player_name = input("Enter player name: ")
games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))

average_score = total_score / games_played

print("\nPlayer:", player_name)
print("\nGames Played:", games_played)
print("\nTotal Score:", total_score)
print("\nAverage Score:", average_score)
