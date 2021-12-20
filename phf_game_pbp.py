# regex expressions
# need to check takeaway string for python compatibility
away = "[:digit:] GvA|[:digit:] TkA|[:digit:] Blk"
fill = "from| by|against|to| and|giveaway|Game|Behind|of |Served|served|Bench|bench"
goalie = "Starting goalie|Pulled goalie|Returned goalie"
fo = "faceoff won"
ice = "Even Strength|Empty Net|Power Play|Extra Attacker|Short Handed"
shots = "Snap shot|Wrist shot|Penalty Shot"
reb = "blocked|saved|failed attempt"
pen = "Holding the Stick|Holding|Tripping|Roughing|Hooking|Interference|Diving|Delay|Cross-Checking|Head Contact|Body Checking|Slashing|Check from Behind Misconduct|Checking from Behind|Checking|Ejection|Too Many Men|Delay of Game|Misconduct|Check|High-Sticking"
type = "Minor|Major"
# need to check score string
score_string = "[:digit:] - [:digit:] [A-Z]+|[:digit:] - [:digit:]"
shoot = "missed attempt against|scores against|Shootout|failed attempt"
# need to check length of penalty string for python compatibility
lgh = "[:digit:] mins|[0-9]+ mins"
abbreviations = "TOR|MIN|BOS|CTW|MET|BUF"
ne = "On Ice"

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from pandas.io import json
import requests as rq
from funcy import pluck
import json as js
from types import SimpleNamespace
from IPython.display import display_html, display_json
import io