# This program pulls player and team data from the NBA API, cleans it,
# and prepares it for insertion into a PostgreSQL database.

# Import necessary modules
from nba_api.stats.static import players  # Module to fetch static player info
from pandas import concat         # For data manipulation                        # For PostgreSQL connect
import time
from helper import *
from sqlalchemy import create_engine


# Initialize a list to store cleaned season-by-season stats
seasons = []

# Fetch active NBA players dictionary
players_list = players.get_active_players()

# format into a dataframe
players_frame = getPlayers(players_list)

# Extract player IDs to loop over
id_list = players_frame["id"]


# Loop through each player ID to get season averages
for i in id_list:
    getSeasonStats(i)
    time.sleep(.5)

# Concatenate all players’ season data into one DataFrame
seasons_frame = concat(seasons, ignore_index=True)


# Display a preview of the final DataFrame
print(seasons_frame.head())
print(seasons_frame.info())
