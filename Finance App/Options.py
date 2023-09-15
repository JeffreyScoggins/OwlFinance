
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import Delta as delta
import Research as research


def option_expiry(symbol):
    tk = yf.Ticker(symbol)
    # Expiration dates
    exps = tk.options
    return exps


def options_chain_call(symbol, date):

    tk = yf.Ticker(symbol)
    r = yf.Ticker("^TNX")

    previousClose = tk.info['previousClose']

    options = pd.DataFrame()
    options = tk.option_chain()
    tmp = []
    for count in options:
        tmp.append(options.calls)
    options = pd.concat(tmp)
    options['expirationDate'] = date
    print(options)
    print(options['expirationDate'])
    tmp = []
    datetime.datetime.today().strftime('%Y-%m-%d')
    #modT = pd.to_datetime(options['expirationDate']) + datetime.timedelta(days = 1) #makes it end of day vs beginning
    #dte =  modT - datetime.datetime.today()
    #dteYearly = (dte.dt.days)



    #Calculate Greeks
    #greeks = delta.BlackScholes(tk.info['previousClose'], options['strike'], previousClose, options['impliedVolatility'], dteYearly,0)
    #add delta column
    #add gamma column


    # Boolean column if the option is a CALL
    print(options)
    options['CALL'] = options['contractSymbol'].str[4:].apply(
        lambda x: "C" in x)
    
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mark'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask
    
    # Drop unnecessary and meaningless columns
    options = options.drop(columns = ['contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'])
    #greekCall(tk, options, dteYearly) #calculates black sholes for calls
    return options
    

def options_chain_put(symbol, date):

    tk = yf.Ticker(symbol)
    r = yf.Ticker("^TNX")

    previousClose = tk.info['previousClose']

    options = pd.DataFrame()
    options = tk.option_chain()
    tmp = []
    for count in options:
        tmp.append(options.puts)
    options = pd.concat(tmp)
    options['expirationDate'] = date
    options
    datetime.datetime.today().strftime('%Y-%m-%d')
    #modT = pd.to_datetime(options['expirationDate']) + datetime.timedelta(days = 1) #makes it end of day vs beginning
    #dte =  modT - datetime.datetime.today()
    #dteYearly = (dte.dt.days)

    #add delta column
    #add gamma column



    
    # Boolean column if the option is a PUT
    options['PUT'] = options['contractSymbol'].str[4:].apply(
       lambda x: "C" in x)
    
    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mark'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask
    
    # Drop unnecessary and meaningless columns
    options = options.drop(columns = ['contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'])
    #greekCall(tk, options, dteYearly)# #calculates black sholes for puts

    return options

def greekCall(tk, options, dteYearly):
    greek = delta.BlackScholes(tk.info['previousClose'], options['strike'], tk.info['previousClose'], options['impliedVolatility'], dteYearly,0)

def greekput(tk, options, dteYearly):
    greeks = delta.BlackScholes(tk.info['previousClose'], options['strike'], tk.info['previousClose'], options['impliedVolatility'], dteYearly,1)