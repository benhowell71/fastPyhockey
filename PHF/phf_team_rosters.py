"""ready to test PHF Team Rosters"""
import requests
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import json
from datetime import datetime
from tqdm import tqdm

# from phf.phf_get_season_id import phf_get_season_id
from phf.phf_league_info import phf_league_info
from phf.helper_functions import phf_get_player_photo

from phf.helpers import (
    ROSTER_NAMES,
    ROSTER_COLUMNS
)

def phf_roster(team: str, season: int) -> pd.DataFrame:
    # team = 'Boston Pride'
    # season_id = phf_get_season_id(season=season)

    teams = phf_league_info(season=season)[4]

    teams = pd.read_csv('phf/logos.csv')
    if season != 2023:
        team_id = teams[teams.name == team].id.item()
    elif season == 2020:
        teams = pd.read_csv('phf/id_2020.csv')
        team_id = teams[teams.team_name == team].id.item()
    else:
        team_id = teams[teams.full_team_name == team].team_id.item()

    base_url = "https://web.api.digitalshift.ca/partials/stats/team/roster?team_id="
    full_url = base_url + str(team_id)

    payload = {
        'Authorization': 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'
    }

    try:
        res = requests.get(full_url, headers=payload)
        data = json.loads(res.content.decode('utf-8'))
        soup = BeautifulSoup(data['content'], 'html.parser')
        players = soup.find_all('table')[0]

        players_df = pd.read_html(str(players))[0]
        players_df = players_df.iloc[:, 0:5]

        names = []
        ids = []
        link = []
        for y in tqdm(players.find_all('a', {'class': 'person-inline'})):
            id = re.search(r"[0-9]+", y["href"])
            player_id = id.group(0)
            name = re.search(r">(.*)<", str(y)).group(1)
            photo_link = phf_get_player_photo(id=player_id)

            link.append(photo_link)
            names.append(name)
            ids.append(player_id)

        info = pd.DataFrame({
            'player_name': names,
            'player_id': ids,
            'player_photo': link
        })

        player_df = players_df.join(info)

        player_df['is_captain'] = np.where(player_df.Name.str.contains('- C'), 1, 0)

        if 'Height' in player_df.columns:
            player_df['height'] = player_df['Height'].str.replace("'|\"", '')
            player_df[['feet', 'inches']] = player_df['height'].str.split(' ', expand=True)
            player_df = player_df.drop(columns=['height'])
        else:
            player_df[['feet', 'inches']] = np.nan
            player_df['Height'] = np.nan
        
        if 'Hometown' not in player_df.columns:
            player_df['Hometown'] = np.nan
            player_df = player_df[['#', 'Name', 'POS', 'Height', 'Hometown', 'player_name', 'player_id',
                        'player_photo', 'is_captain', 'feet', 'inches']]

        if 'Birthdate' not in player_df.columns:
            player_df['Birthdate'] = np.nan
            player_df = player_df[['#', 'Name', 'POS', 'Height', 'Hometown', 'player_name', 'player_id',
                        'player_photo', 'is_captain', 'feet', 'inches', 'Birthdate']]

        player_df.columns = ROSTER_NAMES
        player_df['season'] = season
        player_df['team'] = team
        player_df['team_id'] = team_id
        player_df = player_df[ROSTER_COLUMNS]

        #############################################################
        if len(soup.find_all('table')) > 2:
            staff = soup.find_all('table')[2]
            staff = pd.read_html(str(staff))[0].iloc[:, 0:2]
            staff.columns = ['staff_name', 'staff_role']
        else:
            staff = pd.DataFrame()

        info = [player_df, staff]
        
        return info
    
    except:
        print(f'{datetime.now()}: Invalid arguments or season; please try a season from 2016 onwards.\n I.e. If you want data for the 2015-2016 season, please enter 2016 as the season.')