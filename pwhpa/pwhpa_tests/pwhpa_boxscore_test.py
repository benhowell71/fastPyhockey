import pandas as pd
import numpy as np
from tqdm import tqdm

import time

from pwhpa.pwhpa_boxscore import pwhpa_boxscore
from pwhpa.pwhpa_schedule import pwhpa_schedule

df = pwhpa_schedule()
game = pd.DataFrame()
skaters = pd.DataFrame()
goalies = pd.DataFrame()

for i in tqdm(df[df.home_score.notna()].game_id.tolist()):
    # print(i)
    game_res = pwhpa_boxscore(game_id=i)

    game = game.append(game_res[0])
    skaters = skaters.append(game_res[1])
    goalies = goalies.append(game_res[2])

    time.sleep(3)

