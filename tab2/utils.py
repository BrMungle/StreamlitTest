import numpy as np
import pandas as pd

def get_quantiles(df, column_to_drop, low, high):
    values = df.drop(columns=column_to_drop).stack().dropna().values
    vmin = np.percentile(values, low)
    vmax = np.percentile(values, high)
    return vmin, vmax
