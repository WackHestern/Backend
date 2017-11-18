import database
import stockapi
 
#return true if succeed 
def buy(stockName, amount):
    price = stockapi.getPrice(stockName)
    if (float(price) < 0):
        return False
    
    database.runQuery("INSERT INTO buys (stockname, buyprice, amount) VALUES ('"+stockName+"','"+str(price)+"',"+str(amount)+")")
    
    return True


def sell(stockName, amount):
    pass

def buyData():
    return database.runQueryWithResponse("select * from buys")


def sellData():
    return database.runQueryWithResponse("select * from sells")





