from pathlib import Path

import pandas as pd
import numpy as np
import csv

try:
    import common
    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / 'data'