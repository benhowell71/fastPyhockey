"""
312837 was no data bc it was the Isobel cup that got postponed but was notated as Final
"""
import pandas as pd
import numpy as np
import time

from tqdm import tqdm

from phf.phf_team_box import phf_team_box
from phf.phf_player_box import phf_player_box

df = pd.read_csv('phf/phf_tests/phf_schedule_test.csv')
finished_games = df[df.status == 'Final'].game_id.tolist()

game_data = pd.DataFrame()
skater_data = pd.DataFrame()
goalie_data = pd.DataFrame()

for game_id in tqdm(finished_games):

    game_df = phf_team_box(game_id=game_id)
    players = phf_player_box(game_id=game_id)
    skaters = players[0]
    goalies = players[1]

    skater_data = skater_data.append(skaters)
    goalie_data = goalie_data.append(goalies)
    game_data = game_data.append(game_df)

    time.sleep(3)

skater_data.to_csv('phf/phf_tests/phf_team_player_box_skater_test.csv', index=False)
goalie_data.to_csv('phf/phf_tests/phf_team_player_box_goalie_test.csv', index=False)
game_data.to_csv('phf/phf_tests/phf_team_player_box_game_test.csv', index=False)