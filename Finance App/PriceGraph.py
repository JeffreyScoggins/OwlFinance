import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import Options as options
from datetime import datetime
plt.style.use('seaborn')



def searchreturn():
    interval = [ "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max" ]
    return interval


def oneDay(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('1d')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def fiveDay(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('5d')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def oneMonth(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('1mo')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def threeMonth(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('3mo')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def sixMonth(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('6mo')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def ytd(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('ytd')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')


def oneYear(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('1y')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def twoYear(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('2y')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def fiveYear(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('5y')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def tenYear(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('10y')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')

def max(symbol):

    tk = yf.Ticker(symbol)

    df = tk.history('max')

    plt.figure
    plt.plot(df['Close'])
    plt.savefig('stockprice.png')



