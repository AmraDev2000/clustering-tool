import pandas as pd
import numpy as np

DEFAULT_DATA = np.random.randint(1, 50, size=(2,2), dtype=np.int64)

DEFAULT_DF = pd.DataFrame(DEFAULT_DATA, columns=["x", "y"], dtype=np.int16)

def defineCluster(df = DEFAULT_DF): 

    return df
