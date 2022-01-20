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

def phf_games(season = 2021):

    yr = str(season)

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_boxscore.csv'
    sched = pd.read_csv(raw)
    
    szn = sched[sched.date.str.contains(yr)]

    return szn

def phf_player_box(season = 2022):

    base = (r'https://github.com/saiemgilani/fastRhockey-data/blob/main/phf/player_box/csv/player_box_' + str(season) + '.csv.gz')

    box = pd.read_csv(base)
