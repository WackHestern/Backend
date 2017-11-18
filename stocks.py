import database
import stockapi
import users
 
#return true if succeed 
def buy(stockName, amount):
    price = stockapi.getPrice(stockName)
    
    #make sure price is valid
    if (float(price) < 0):
        print ("failed price check:" + str(price))
        return "fail"
    
    availFunds = float(users.getAvailableFunds())
    cost= float(amount) * float(price)
    #make sure user has enough funds and update funds after buying
    if  cost > availFunds:
        return "insufficient funds"
    
    if not users.updateFunds(availFunds -cost):
        print ("Can't update DB funds" )
        return "fail" 
    
    database.runQuery("INSERT INTO buys (stockname, buyprice, amount) VALUES ('"+stockName+"','"+str(price)+"',"+str(amount)+")")
    
    return "success"


def sell(stockName, amount):
    pass

def buyData():
    return database.runQueryWithResponse("select * from buys")


def sellData():
    return database.runQueryWithResponse("select * from sells")





