import pandas as pd

video_games = pd.read_csv('video_games_raw.csv')

print("VIDEO GAME CATALOG MANAGER")

row = int(input("Which row would you like to evaluate?: "))

if row in video_games.index:
    print("Selected Video Game: ")
    print(video_games.iloc[row])

    status = input("Enter a new status (Backlog, Playing, Completed, Dropped): ")

    if 'Status' not in video_games.columns:
        video_games['Status'] = ""



else: 
    print(f"Row {row} doesn't exist. Valid rows are 0 to {len(video_games) - 1}.")