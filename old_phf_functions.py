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

#fr_stats = "http://www.stats.ffbs.fr/2021/division1/stats/lgplyrs.htm#leagp.anl"

#fr_page = rq.get(fr_stats)

#df = pd.read_html(fr_stats)

#pitch = df[3]
#pitch.columns = pitch.iloc[0]
#pitch = pitch[1:]

#pitch.sort_values(by = 'so', ascending=False)

game_id = 368719

def phf_pbp(game_id):

    base_url = 'https://web.api.digitalshift.ca/partials/stats/game/play-by-play?game_id='

    full_url = base_url + str(game_id)

    auth_ticket = 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'

    r = rq.get(full_url, headers={'Authorization': auth_ticket})

    r.content

    # pd.read_json(rt)

    content = js.loads(r.content)
    
    r.content[:100]
    r.text[:100]
    r.json()

    rt = r.json()
    print(rt)

    soup = bs(r.content, 'html.parser')
    bs(content, 'html.parser')

    tbl = soup.find()

    pd.read_html(str(tbl))[0]

    df = r.content

    

    df = pd.DataFrame.from_dict(rt, orient='index')

    pd.read_csv(io.StringIO(df.decode('utf-8')))