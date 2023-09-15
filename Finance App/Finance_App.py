import os
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import Options as options
import Delta as delta
import PriceGraph as priceGraph
import Research as research
from datetime import datetime
plt.style.use('seaborn')

print ('Welcome to FinancePy!\n')


tickerInput = input('Enter your ticker symbol: ')


ticker = yf.Ticker(tickerInput)


for e in ticker.info:
    print(e, ': ', ticker.info[e],'\n')
priceGraph.threeMonth(tickerInput)

expiry = ticker.options #returns options dictionary of all options data sorted by expiry
count = 1
optionsList = []
for e in expiry: #for loop for every options expiration date found
    print(count,e,'\n')
    count += 1
    optionsList.append(e) #adds entry for every new one found
expDate = input('Please select the data numbered\nPress E to go back\n')

expiry = int(expDate) - 1
dfCall = options.options_chain_call(tickerInput, optionsList[expiry])
dfPut = options.options_chain_put(tickerInput, optionsList[expiry])
#dfPrice = priceGraph.PriceGraph(entry) Shows 6 month line graph
plt.plot(dfCall['strike'], dfCall['volume'], 'g.-', label="Calls")
plt.plot(dfPut['strike'], dfPut['volume'], 'r.-', label="Puts")
plt.xlabel('Strikes')
plt.ylabel('Volume')
#plt.title('Weekly Call/Put Volume for {}'.format(dfCall['expirationDate'])) 
plt.savefig('options.png')
