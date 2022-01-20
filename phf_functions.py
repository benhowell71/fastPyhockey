import pandas as pd
import numpy as np
import csv

def phf_pbp(game_id = 368719):

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_play_by_play.csv'
    pbp = pd.read_csv(raw)
    game_pbp = pbp[pbp.game_id == game_id]

    return game_pbp

# team = 'tor'

def phf_games(season = 2021, team):

    yr = str(season)

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_boxscore.csv'
    sched = pd.read_csv(raw)

    if 'team' in globals():
        szn = sched[(sched.date.str.contains(yr)) & (sched.team = team)]
    else: 
        szn = sched[sched.date.str.contains(yr)]