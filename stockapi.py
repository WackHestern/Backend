import urllib.request, json 
import datetime
 
    
def getLast10DayPrices(stockName):
    ret = []
    stockName=stockName.upper()
    
    try:
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stockName+"&apikey=5UQ13GR7ST5S6ZKB") as url:
            data = json.loads(url.read().decode())
            
        
        data = data["Time Series (Daily)"]
        times = data.keys()
        times= [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in times]
        times = sorted(times)
        times = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in times]
        for i in range (len(times)-1, max(0, len(times)-11),-1): #for each day
            day = times[i]
            price = data[day]["2. high"]
            ret.append([day,price])
            
        
    except Exception:
        print ("failed to get last 10 days of data")
        return []
    return ret[::-1] #return in ascending order
    

    
def getPrice(stockName):
    stockName = stockName.upper()
    
    try:
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stockName+"&interval=1min&apikey=5UQ13GR7ST5S6ZKB") as url:
            data = json.loads(url.read().decode())
        return data["Time Series (1min)"][data["Meta Data"]["3. Last Refreshed"]]["4. close"]
        
    except Exception:
        return -1
