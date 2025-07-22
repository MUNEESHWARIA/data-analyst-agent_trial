import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def make_plot(df):
    fig, ax = plt.subplots()
    ax.scatter(df["Rank"], df["Worldwide gross"])
    z = np.polyfit(df["Rank"], df["Worldwide gross"], 1)
    p = np.poly1d(z)
    ax.plot(df["Rank"], p(df["Rank"]), "r--")
    ax.set_xlabel("Rank")
    ax.set_ylabel("Worldwide Gross")
    ax.set_title("Rank vs Gross")

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=150)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded}"
