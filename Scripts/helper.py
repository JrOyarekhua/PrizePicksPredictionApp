# helper functions to retrive statistics
# get specific imports
from nba_api.stats.static import teams    # Module to fetch static team info
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear  # To get season-by-season stats
import pandas as pd                       # For data manipulation
import time
from nba_api.stats.endpoints import TeamDashboardByGeneralSplits

def getPlayers(players_dict):
    # Reformat list of player dicts into a list of single-row DataFrames
    formatted_list = [{key: [val] for key, val in i.items()} for i in players_dict]
    # Convert each dict to a DataFrame, then concatenate all into one DataFrame
    players_frame = [pd.DataFrame.from_dict(i) for i in formatted_list]
    players_frame = pd.concat(players_frame, ignore_index=True)
    # Lowercase all string values for consistency
    players_frame = players_frame.map(lambda x: x.lower() if isinstance(x, str) else x)
    return players_frame

def getSeasonStats(player_id):
    retries = 3  # Retry up to 3 times if there's a connection error
    for attempt in range(retries):
        try:
            # Fetch the season-by-season data for this player
            player_dict = PlayerDashboardByYearOverYear(player_id).get_dict()
            by_year = player_dict['resultSets'][1]

            # Convert to DataFrame
            player_frame = pd.DataFrame(by_year["rowSet"], columns=by_year["headers"])

            # Drop unneeded columns: static fields and anything past column index 33
            to_drop = ["GROUP_SET", "MAX_GAME_DATE"] + player_frame.columns.to_list()[34:]
            player_frame.drop(columns=to_drop, inplace=True)

            # Convert all column names to lowercase for consistency
            player_frame.columns = player_frame.columns.str.lower()

            # attach id as a seperate column
            player_frame['player_id'] = player_id

            # rename grouo value to season_id
            player_frame = player_frame.rename(columns={'group_value': 'season_id'})

            # attach season start and end columns
            player_frame["season_start"] = player_frame["season_id"].str[:4].astype(int)
            player_frame["season_end"] = player_frame["season_id"].str[-2:].astype(int)
            # Fix century if needed (e.g., for "1999-00")
            player_frame["season_end"] = player_frame.apply(
                lambda row: row["season_end"] + 2000 if row["season_end"] < 50 else row["season_end"] + 1900,
                axis=1
            )

            print(f"player {player_id} successfully retrieved")
            return player_frame

        except Exception as e:
            print(f"Attempt {attempt + 1} failed for player {player_id}: {e}")
            time.sleep(2)  # Wait before retrying
    else:
        # Only executes if all retry attempts fail
        print(f"player {player_id} failed after 3 attempts")

def getTeams(teams_list):
    teams_frame = []
    for i in range(len(teams_list)):
        formatted_dict = {key:[val] for key, val in teams_list[i].items()}
        df = pd.DataFrame.from_dict(formatted_dict)
        teams_frame.append(df)
    teams_frame = pd.concat(teams_frame, ignore_index=True)
    return teams_frame



def getTeamStats(team_id):
    retries = 3
    for attempt in range(retries):
        try:
            # logic to retrive stats for an individual team
            res = TeamDashboardByGeneralSplits(team_id).get_dict()['resultSets'][0]
            team_frame = pd.DataFrame(res['rowSet'], columns=res['headers'])
            print(team_frame.shape)
            print(team_frame.head())
            team_frame = team_frame.iloc[:,1:29]
            team_frame.columns = team_frame.columns.str.lower() # make all columns lower case
            team_frame.rename(columns={'group_value': 'team_id'}, inplace=True)  # rename group value
            return team_frame
        except Exception as e:
            print(f"Attempt {attempt + 1} failed for team {team_id}")
            print(e)
            time.sleep(2)
    raise Exception(f"Attempt failed for team {team_id}")


