import pandas as pd
import requests
import numpy as np
import re
from bs4 import BeautifulSoup
import json
from datetime import datetime

from PHF.phf_league_info import phf_league_info
from PHF.helpers import STANDINGS_COLS

def phf_standings(season: int) -> pd.DataFrame:

    logos = pd.read_csv('PHF/logos.csv')

    lg_info = phf_league_info(season=season)
    lg = lg_info[0]
    season_df = lg[lg.single_season == season]
    season_id = season_df.season_id.item()
    league_id = lg_info[3] # 13893 for 2023
    base_url = "https://web.api.digitalshift.ca/partials/stats/standings/table?division_id=" + str(league_id) + "&league_toggle=division&season_id="
    full_url = base_url + str(season_id)

    payload = {
        'Authorization': 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'
    }

    try:
        res = requests.get(full_url, headers=payload)
        data = json.loads(res.content.decode('utf-8'))
        soup = BeautifulSoup(data['content'], 'html.parser')
        tbody = soup.find_all('table')[0]

        standings = pd.read_html(str(tbody))[0]
        standings['Team'] = standings.Team.str.replace("[0-9]+", "")
        # standings['team_abbrev'] = standings.Team.str[-3:]
        standings['Team'] = standings.Team.str[:-3]

        standings.columns = STANDINGS_COLS
        standings = standings.merge(logos, how='left', left_on='team_name', right_on='full_team_name')

        return standings
    except:
        print(f'{datetime.now()}: Invalid arguments or season; please try a season from 2016 onwards.\n I.e. If you want data for the 2015-2016 season, please enter 2016 as the season.')
