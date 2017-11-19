import database
import stockapi
import users
import stocks
from datetime import datetime

#returns the count of a stock on a certain day
def getCntOnDay(stockName, day):
    cnt=0
    day = day.split("-")
    day = int("".join(day))
    
    try:
        buys = stocks.buyData()
        sells = stocks.sellData()
        print (buys)
        for b in buys:
            if b[0] != stockName:
                continue
            date = b[3]
            print (date)
            date = date.isoformat()
            print (date)
            date = date[0:11].split("-")
            print (date)
            date = int("".join(date))
            print (date)
            
            if date <= day:
                cnt +=int( b[2])
        
    except Exception:
        print ("failed to find count of stock on day")
        return 0
    
    if cnt<0:
        return 0
    return cnt

#return of list of unique stock names
def listStocks():
    ret = []
    try:
        ret = database.runQueryWithResponse("SELECT DISTINCT stockName FROM buys;")
        ret = [x[0] for x in ret]
        print (ret)
    except Exception:
        print ("failed to generate list of unique stock names")
        return []
    
    return ret

def generateDataHistory():
    #for each day
    #list of {stocks : value}
    stockNames = listStocks()
    ret = {} #key: day value: [{stock:value}, {}...]
    
    for sn in stockNames:
        dd = stockapi.getLast10DayPrices(sn) 
        for dp in dd:
            day = dp[0]
            price = float(dp[1])
            cnt = float(getCntOnDay(sn, day))
            
            if day not in ret:
                ret[day] = []
            if cnt >0:
                ret[day].append({sn: price * cnt})
    print (ret)
    return ret
    