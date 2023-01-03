"Works!"
import pandas as pd
import numpy as np
import time

from phf.phf_standings import phf_standings

df = pd.DataFrame()

for year in np.arange(2016, 2023 + 1):
    # print(year)
    df = pd.concat([df, phf_standings(season=year)])

    time.sleep(3)

df.to_csv('phf/phf_tests/phf_standings_test.csv', index=False)

# fix 2022-2023
# fix 2019-2020