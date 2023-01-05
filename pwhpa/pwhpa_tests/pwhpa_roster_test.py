import pandas as pd
import numpy as np
from tqdm import tqdm

import time

from pwhpa.pwhpa_roster import pwhpa_roster

roster = pwhpa_roster(team='all')