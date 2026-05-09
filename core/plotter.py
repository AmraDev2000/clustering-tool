import matplotlib.pyplot as plt
import pandas as pd

def plotDots(df: pd.DataFrame):
    scatter = plt.scatter(df["x"], df["y"])
    fig = scatter.figure
    return fig
    