Player=input("Player: ")
GamesPlayed=int(input("Games Played: "))
Score=[]
TotalScore=0
AverageScore=0
for i in range(GamesPlayed):
    s = int(input(f"Enter Score for game {i+1}: "))
    TotalScore = TotalScore + s

print(f"Player: {Player}")
print(f"Games Played: {GamesPlayed}")
print(f"Total Score: {TotalScore}")
print(f"Average Score: {TotalScore/GamesPlayed}")


