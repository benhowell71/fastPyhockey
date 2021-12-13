import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import requests as rq
from funcy

game_id = 368719

def phf_pbp(game_id):

    base_url = 'https://web.api.digitalshift.ca/partials/stats/game/play-by-play?game_id='

    full_url = base_url + str(game_id)

    auth_ticket = 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'

    r = rq.get(full_url, headers={'Authorization': auth_ticket})
    
    r.content[:100]

    rt = r.json()

    soup = bs(r.content, 'html.parser')