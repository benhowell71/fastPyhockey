import requests
import json
import re

import numpy as np

def phf_get_player_photo(id: int):
    # id = 627750
    base_url = "https://web.api.digitalshift.ca/partials/stats/player?player_id="
    full_url = base_url + str(id)

    payload = {
        'Authorization': 'ticket="4dM1QOOKk-PQTSZxW_zfXnOgbh80dOGK6eUb_MaSl7nUN0_k4LxLMvZyeaYGXQuLyWBOQhY8Q65k6_uwMu6oojuO"'
    }

    try:
        res = requests.get(full_url, headers=payload)
        data = json.loads(res.content.decode('utf-8'))

        link = re.search("https://img.shiftstats.com/dcd7c2ef-0bf7-4a7e-a22f-e1e1a76f936c/person-photo_url(.*?).png", str(data['content'])).group(0)

    except:
        link = np.nan
    
    return link