import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def process_game(game_info) -> pd.DataFrame:

    date_time = game_info[0].text[0:19]
    date = game_info[0].text[19:len(game_info[0].text)]

    home_tm = game_info[1].text.strip()
    away_tm = game_info[3].text.strip()

    if 'am' in game_info[2].text or 'pm' in game_info[2].text:
        start_time = game_info[2].text
        home_score = np.nan
        away_score = np.nan
    else:
        res = game_info[2].text.split('-')
        home_score = int(res[0].strip())
        away_score = int(res[1].strip())
        start_time = np.nan

    location = game_info[4].text
    game_link = game_info[5].find_all('a')[0].get('href')
    game_id = game_link.replace('https://stats.pwhpa.com/event/', '')
    game_id = game_id.replace('/', '')

    winner = np.where(home_score > away_score, home_tm, np.where(away_score > home_score, away_tm, 'tie')).item()

    game_df = pd.DataFrame({
        'game_date': [date],
        'game_time': [date_time],
        'game_id': [game_id],
        'winner': [winner],
        'home_team': [home_tm],
        'home_score': [home_score],
        'away_team': [away_tm],
        'away_score': [away_score],
        'start_time': [start_time],
        'location': [location],
        'game_link': [game_link]
    })

    return game_df

def process_member(player_info):

    jersey = player_info[0].text
    name = player_info[1].text
    player_link = player_info[1].find_all('a')[0].get('href')
    names = name.split(' ')
    first_name = names[0]
    last_name = names[1]
    link = player_info[2].find_all('a')[0].get('href')
    team = link.replace('https://stats.pwhpa.com/team/', '')
    team_id = team.replace('/', '')

    position = player_info[3].text
    dob = player_info[4].text
    age = player_info[5].text
    home_town = player_info[6].text
    college = player_info[7].text

    player_df = pd.DataFrame({
        'player_name': [name],
        'first_name': [first_name],
        'last_name': [last_name],
        'team_id': [team_id],
        'position': [position],
        'number': [jersey],
        'date_of_birth': [dob],
        'age': [age],
        'home_town': [home_town],
        'college': [college],
        'player_page': [player_link]
    })

    return player_df