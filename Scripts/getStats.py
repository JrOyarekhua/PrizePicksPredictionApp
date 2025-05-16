# This program will pull player data from the nba api and store it in a postgresDB

# Import necessary modules
from nba_api.stats.static import players,teams  # Module to fetch static player info
from pandas import concat         # For data manipulation                        # For PostgreSQL connect
import time
from helper import *


# Initialize a list to store cleaned season-by-season stats
season = []
team = []

# Fetch active NBA players dictionary
players_list = players.get_active_players()
teams_list = teams.get_teams()

# format into a dataframe
players_frame = getPlayers(players_list)
teams_frame = getTeams(teams_list)


# Extract player IDs to loop over
player_id_list = players_frame["id"]
team_id_list = teams_frame["id"]

for i in team_id_list:
    t_frame = getTeamStats(i) # should return the formatted teams frame to append to the table
    team.append(t_frame)
    print(f'team {i} sucessfully added')
    time.sleep(.5)

# Loop through each player ID to get season averages
# for i in player_id_list:
#     s_frame = getSeasonStats(i)
#     season.append(s_frame)
#     print(f'player {i} sucessfully added')
#     time.sleep(.5)



# seasons_frame = concat(season, ignore_index=True)
teams_frame = concat(team, ignore_index=True)
# seasons_frame.to_csv("/Users/jroyarekhua/nba_predictions/data/player_season.csv", index=False)
teams_frame.to_csv("/Users/jroyarekhua/nba_predictions/data/team.csv", index=False)

