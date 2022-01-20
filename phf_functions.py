import pandas as pd
import numpy as np
import csv

def phf_pbp(game_id = 368719):

    raw = 'https://raw.githubusercontent.com/saiemgilani/fastRhockey-data/main/phf/phf_play_by_play.csv'
    pbp = pd.read_csv(raw)
    game_pbp = pbp[pbp.game_id == game_id]

    return game_pbp