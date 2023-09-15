
def research(ticker):

    previousClose = ticker.info['previousClose']
    twoHundredEMA = ticker.info['twoHundredDayAverage']
    marketCap = ticker.info['marketCap']
    fiftyTwoWeekHigh = ticker.info['fiftyTwoWeekHigh']
    fiftyTwoWeekLow = ticker.info['fiftyTwoWeekLow']
    sharesOutstanding = ticker.info['sharesOutstanding']
    floatShares = ticker.info['floatShares']
    forwardPE = ticker.info['forwardPE']
    forwardEPS = ticker.info['forwardEps']
    bookValue = ticker.info['bookValue']
    priceToBook = ticker.info['priceToBook']
    shortPercentageOfFloat = ticker.info['shortPercentOfFloat']

    print("Previous close: ", previousClose)
    print("200 EMA :", twoHundredEMA)
    print("Market Cap :", marketCap)
    print("52 Week High :", fiftyTwoWeekHigh)
    print("52 Week Low :", fiftyTwoWeekLow)
    print("Shares Outstanding :", sharesOutstanding)
    print("Float Shares :", floatShares)
    print("Forward P/E :", forwardPE)
    print("Forward EPS :", forwardEPS)
    print("bookValue :", bookValue)
    print("Price to Book :", priceToBook)
    print("Short Percentage of Float :", shortPercentageOfFloat)

def getPreviousClose(ticker):
    previousClose = ticker.info['previousClose']
    return previousClose
