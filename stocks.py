import database
import stockapi
 
#return true if succeed 
def buy(stockName, amount):
    price = stockapi.getPrice(stockName)
    if (price < 0):
        return False
    
    database.runQuery(runQuery("INSERT INTO buys ("+stockName+", buyprice, amount) VALUES ('"+stockName+"','"+str(price)+"',"+str(amount)+")" ))
    
    return True


def sell(stockName, amount):
    pass

def data():
    return database.runQueryWithResponse("select * from buys") + database.runQueryWithResponse("select * from sells")





