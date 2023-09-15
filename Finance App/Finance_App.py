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
while True: #infinite loop
    entry = input('Enter 1 for financial research, or 2 for options analysis\n')
    if (entry == '1'):

        ticker = input('Enter your ticker symbol: ')
        while True: #infinite loop

            ticker = yf.Ticker(ticker)
            count = 1
            stockList = []
            for e in ticker.info:
                print(count,e,'\n')
                count += 1
                stockList.append(e) #adds new entry to list for every new value found in dictionary
            text = input('Please select the data numbered\nPress E to go back\n')
            if (text == 'e'):
                os.system('cls') #clears screen
                break #goes back one menu
            search = int(text) - 1
            print(ticker.info[stockList[search]])

    



    if (entry == '2'):
        entry = input("Enter your ticker symbol: ")
        while True: #infinite loop
            '''
            #Prints every data point in ticker.info
            for key,value in printValue.items():
                print(key,": ",value)

            print("")
            '''
            expiry = options.option_expiry(entry)
            count = 1
            optionsList = []
            for e in expiry: #for loop for every options expiration date found
                print(count,e,'\n')
                count += 1
                optionsList.append(e) #adds entry for every new one found
            expDate = input('Please select the data numbered\nPress E to go back\n')
            if (expDate == 'e'):
                os.system('cls') #clears screen
                break #goes back one menu
            expiry = int(expDate) - 1
            dfCall = options.options_chain_call(entry, optionsList[expiry])
            dfPut = options.options_chain_put(entry, optionsList[expiry])
            #dfPrice = priceGraph.PriceGraph(entry) Shows 6 month line graph
            plt.plot(dfCall['strike'], dfCall['volume'], 'g.-', label="Calls")
            plt.plot(dfPut['strike'], dfPut['volume'], 'r.-', label="Puts")
            plt.xlabel('Strikes')
            plt.ylabel('Volume')
            plt.title('Weekly Call/Put Volume for {}'.format(dfCall['expirationDate'])) 
            plt.show()
    else:
        print("Invalid Entry, please re-enter")