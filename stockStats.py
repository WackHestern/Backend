import database
import stockapi
import users

#returns the count of a stock on a certain day
def getCntOnDay(stockName, day):
    pass


#return of list of unique stock names
def listStocks():
    ret = []
    try:
        ret = database.runQueryWithResponse("SELECT DISTINCT stockName FROM buys;")
        print (ret)
    except Exception:
        print "failed to generate list of unique stock names"
        return []
    
    return ret

def generateDataHistory():
    #for each day
    #list of {stocks : value}
    stockNames = listStocks()
    ret = {} #key: day value: [{stock:value}, {}...]
    
    for sn in stockNames:
        #dd = stockapi.getLast10DayPrices(sn) 
        pass
        
    
    
    return ret
    