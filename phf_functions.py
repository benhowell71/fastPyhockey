from urllib import response
import pandas as pd
import numpy as np
import csv
from io import BytesIO
import requests

def phf_pbp(game_id = 368719):

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_play_by_play.csv'
    pbp = pd.read_csv(raw)
    game_pbp = pbp[pbp.game_id == game_id]

    return game_pbp

# team = 'tor'

def phf_games(season = 2022):

    yr = str(season)

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/schedules/csv/phf_schedule_' + yr + '.csv'
    sched = pd.read_csv(raw)
    
    szn = sched[sched.date.str.contains(yr)]

    return szn

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
