from urllib import response
import pandas as pd
import numpy as np
import csv
from io import BytesIO
import requests

def phf_pbp(game_id = 368719):
    """Load play-by-play data for the Premier Hockey Federation for a given game.
    Example: 
        `pbp = phf_pbp(game_id = 368719)`
    Args:
        game_id (int): Used to define different games. Recommend using `phf_games` to find the game_id of interest. Play-by-play data is available for 2016, 2020, 2021, and 2022.
    Returns:
        pd.DataFrame: Pandas dataframe containing play-by-play data for the requested game.
    Raises:
        Error: If `season` is less than 2016. If `season` < 2016, phf_games returns an empty list
    """
    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_play_by_play.csv'
    pbp = pd.read_csv(raw)
    game_pbp = pbp[pbp.game_id == game_id]

    if len(game_pbp) == 0:
        print("That is not a valid game ID, please try another.")
        print("It is recommended to use `phf_games(season = 2022)` to pull game_ids that you are interested in.")
        print("Play-by-play data is only available for the 2016, and 2020-2022 seasons.")

    return game_pbp

phf_pbp(game_id=2)

# team = 'tor'
def phf_games(season = 2022):
    """Load game meta data for the Premier Hockey Federation for a given season.
    Example: 
        `season_data =  phf_games(season = 2022)`
    Args:
        season (int): Used to define different seasons. 2016 is the earliest available season.
    Returns:
        pd.DataFrame: Pandas dataframe containing game-meta data for the requested seasons.
    Raises:
        Error: If `season` is less than 2016. If `season` < 2016, phf_games returns an empty list
    """
    if int(season) < 2016:
        print("SeasonNotFoundError: Season cannot be less than 2016")

        # exit()
        szn = []
    else:

        yr = str(season)

        raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/schedules/csv/phf_schedule_' + yr + '.csv'
        sched = pd.read_csv(raw)
        
        szn = sched[sched.date_group.str.contains(yr)]
    
    return szn

phf_games(season=2000)

def phf_team_box(season = 2022, game_id = 420405):
    base = 'https://github.com/saiemgilani/fastRhockey-data/blob/main/phf/team_box/csv/team_box_' + str(season) + '.csv.gz'
    query = {'raw': 'true'}
    respo = requests.get(base, params=query)
    fp = BytesIO(respo.content)

    box = pd.read_csv(fp, compression='gzip')
    team_box = box[box.game_id == game_id]

    return team_box

def phf_player_box(season = 2022, game_id = 420405):

    base = 'https://github.com/saiemgilani/fastRhockey-data/blob/main/phf/player_box/csv/player_box_' + str(season) + '.csv.gz'
    query = {'raw': 'true'}
    respo = requests.get(base, params=query)
    fp = BytesIO(respo.content)

    box = pd.read_csv(fp, compression='gzip')
    game_box = box[box.game_id == game_id]

    return game_box
