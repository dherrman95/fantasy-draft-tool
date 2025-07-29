import pandas as pd

# Load nflfastR 2024 play-by-play data directly from GitHub
url = 'https://github.com/nflverse/nflverse-data/releases/download/play_by_play_2024/play_by_play_2024.parquet'

# Load the data into a DataFrame
df = pd.read_parquet(url, engine='pyarrow')

# Filter for plays with passing stats
qbs = df[df['pass_attempt'] == 1]

# Aggregate passing yards by player
qb_stats = (
    qbs.groupby('passer_player_name')['passing_yards']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 QBs by Passing Yards (2024):")
print(qb_stats)

python fantasy_stats.py
