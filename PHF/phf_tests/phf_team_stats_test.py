"""works and quick!"""
import pandas as pd
import numpy as np
import time

from tqdm import tqdm

from phf.phf_team_stats import phf_team_stats

df = pd.read_csv('phf/phf_tests/phf_standings_test.csv')

skater_data = pd.DataFrame()
goalie_data = pd.DataFrame()

for i in tqdm(np.arange(0, len(df))):
    team_yr = df.iloc[[i]]

    team = team_yr.team_name.item()
    season = team_yr.season.item()

    if team == 'Toronto Six' and season == 2020:
        continue

    team_stats = phf_team_stats(team=team, season=season)
    skater_data = skater_data.append(team_stats[0])
    goalie_data = goalie_data.append(team_stats[1])

    time.sleep(3)

skater_data.to_csv('phf/phf_tests/phf_team_stats_skater_test.csv', index=False)
goalie_data.to_csv('phf/phf_tests/phf_team_stats_goalie_test.csv', index=False)
