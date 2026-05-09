import pandas as pd
import numpy as np


def csv(file):

    df = pd.read_csv(file)

    return df

def text(file):

    text = file.readlines()

    rows = []

    for line in text:
        line = line.decode()
        splitted = line.split(",")

        x = int(splitted[0].strip())
        y = int(splitted[1].strip())
        rows.append({x,y})

    df = pd.DataFrame(rows, columns=["x", "y"], dtype=np.int64)

    return df