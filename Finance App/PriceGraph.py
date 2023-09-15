import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import Options as options
from datetime import datetime
plt.style.use('seaborn')


def PriceGraph(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('3mo')

    plt.figure
    plt.plot(df['Close'])
    plt.show()
