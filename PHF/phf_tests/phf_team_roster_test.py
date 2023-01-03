"""Works!"""
import pandas as pd
import numpy as np
import time

from tqdm import tqdm

from phf.phf_team_rosters import phf_roster

df = pd.read_csv('phf/phf_tests/phf_standings_test.csv')

players = pd.DataFrame()
staff = pd.DataFrame()

for i in tqdm(np.arange(0, len(df))):
    team_yr = df.iloc[[i]]

    team = team_yr.team_name.item()
    season = team_yr.season.item()

    if team == 'Toronto Six' and season == 2020:
        continue

    roster = phf_roster(team=team, season=season)
    players = players.append(roster[0])
    staff = staff.append(roster[1])

    time.sleep(3)

# players.to_csv('phf/phf_tests/phf_team_roster_players_test.csv', index=False, mode='a', header='false')
players.to_csv('phf/phf_tests/phf_team_roster_players_test2.csv', index=False)
staff.to_csv('phf/phf_tests/phf_team_roster_staff_test.csv')