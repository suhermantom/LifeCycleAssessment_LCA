from pathlib import Path

import pandas as pd
import numpy as np
import csv

try:
    import common
    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / 'data'

techMat_csv = DATA / 'hw6_tech_matrix.csv'
fdQ2_csv = DATA / 'hw6_fd_q2.csv'
fdQ5_csv = DATA / 'hw6_fd_q5.csv'

for entry in DATA.iterdir():
    if entry.is_file():
        print(entry.name)