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
import http.client
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
import string

game_id = 368719

def phf_game_details(game_id):

    base_url = "https://web.api.digitalshift.ca/partials/stats/game?game_id="
    full_url = base_url + str(game_id)

    auth_ticket = 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'

    raw = rq.get(full_url, headers={'Authorization': auth_ticket})
    soup = bs(raw.content, 'html.parser')

    pd.read_html(raw.text)

    soup.find_all('.flex-row.flex-pcenter')

    



def phf_pbp(game_id):

    base_url = 'https://web.api.digitalshift.ca/partials/stats/game/play-by-play?game_id='
    full_url = base_url + str(game_id)

    auth_ticket = 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'

    raw = rq.get(full_url, headers={'Authorization': auth_ticket})

    soup = bs(raw.content, 'html.parser')

    # soup.current_data

    p = js.loads(raw.content)

    raw.content[:50]
    p[50:]

    q = p['content']

    # type(q)

    data_list = pd.read_html(q)

    np.size(data_list[0], axis=1)
    np.size(data_list[1], axis=1)

period = data_list[0]

period = period.set_axis(['play_type', 'team', 'time', 'description'], axis = 1)

period['scoring_team_abbrev'] = 'NaN'
period['scoring_team_on_ice'] = 'NaN'
period['defending_team_abbrev'] = 'NaN'
period['defending_team_on_ice'] = 'NaN'

tm = 'Boston PrideBOS'

period['team'] = period.team.str.extract(r'(TOR|MIN|BOS|CTW|MET|BUF)', expand = True)