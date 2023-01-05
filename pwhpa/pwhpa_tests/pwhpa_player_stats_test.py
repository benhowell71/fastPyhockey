import pandas as pd
import numpy as np
from tqdm import tqdm

import time

from pwhpa.pwhpa_player_stats import pwhpa_player_stats

skaters = pwhpa_player_stats(position='skaters')
goalies = pwhpa_player_stats(position='goalies')