"""Works!"""
import pandas as pd
import numpy as np
import time

from tqdm import tqdm

from phf.phf_leaders import phf_leaders

seasons = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
skater_data = pd.DataFrame()
goalie_data = pd.DataFrame()

for yr in tqdm(seasons):

    skater_df = phf_leaders(player_type='players', season=yr)
    goalie_df = phf_leaders(player_type='goalies', season=yr)

    skater_data = skater_data.append(skater_df)
    goalie_data = goalie_data.append(goalie_df)

    time.sleep(3)

skater_data.to_csv('phf/phf_tests/phf_leaders_skaters.csv', index=False)
goalie_data.to_csv('phf/phf_tests/phf_leaders_goalies.csv', index=False)