"Works!"
import pandas as pd
import numpy as np
import time

from phf.phf_schedule import phf_schedule

df = pd.DataFrame()

for year in np.arange(2016, 2023 + 1):
    # print(year)
    df = pd.concat([df, phf_schedule(season=year)])

    time.sleep(3)

df.to_csv('phf/phf_tests/phf_schedule_test.csv', index=False)