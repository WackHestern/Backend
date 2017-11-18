import urllib.request, json 

def getPrice(name):
    data={}
    
    try:
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+name+"&interval=1min&apikey=5UQ13GR7ST5S6ZKB ") as url:
            try:
                data = json.loads(url.read().decode())
            except Exception:
                return -1
    except Exception:
        return -1
    
    try:
        return data["Time Series (1min)"][data["Meta Data"]["3. Last Refreshed"]]["4. close"]
    except:
        return -1


#print (getPrice("TSLA"))