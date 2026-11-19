import pandas as pd

video_games = pd.read_csv('video_games_raw.csv')

print("VIDEO GAME CATALOG MANAGER")

row = int(input("Which row would you like to evaluate? (0-14): "))

if row in video_games.index:
    game = video_games.iloc[row]
    print("Selected Game:")
    print(f"Title: {game['Title']}")
    print(f"Platform: {game['Platform']}")
    print(f"Genre: {game['Genre']}")
    print(f"Rating: {game['Rating']}")
    print(f"Current Status: {game['Status']}")

    status = input("Enter a new status (Backlog, Playing, Completed, Dropped): ")
    video_games.at[row, 'Status'] = status

    video_games['Recommended'] = 'No'
    video_games.loc[(video_games['Rating'] >= 8) & (video_games['Price'] <= 40), 'Recommended'] = 'Yes'
    print("Recommended Games:")
    print(video_games.query("Recommended == 'Yes'")[['Title', 'Platform', 'Price', 'Rating']])

    video_games.to_csv('video_games_cleaned.csv', index=False)
    print("The catalog has been updated.")
    print("Saved to video_games_cleaned.csv.")

else: 
    print(f"Row {row} doesn't exist. Valid rows are 0 to {len(video_games) - 1}.")