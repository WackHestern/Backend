import urllib.request, json 

def getPrice(name):
    data={}
    
    name=name.upper()
    
    try:
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+name+"&interval=1min&apikey=5UQ13GR7ST5S6ZKB ") as url:
            data = json.loads(url.read().decode())
        return data["Time Series (1min)"][data["Meta Data"]["3. Last Refreshed"]]["4. close"]
        
    except Exception:
        return -1
    
