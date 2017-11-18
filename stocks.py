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
    price = float(stockapi.getPrice(stockName))
    
    if (price < 0):
        print ("failed price check:" + str(price))
        return "fail"
    availFunds = availFunds = float(users.getAvailableFunds())
    
    curStockCnt= int(getStockCntByName(stockName))
    amount = int(amount)
    if curStockCnt < amount:
        return "insufficient stocks"
    
    if not users.updateFunds(availFunds + (amount * price)):
        print ("Can't update DB funds" )
        return "fail" 
    
    database.runQuery("INSERT INTO sells (stockname, sellprice, amount) VALUES ('"+stockName+"','"+str(price)+"',"+str(amount)+");")
    
    return "success"
    

def buyData():
    try:
        return database.runQueryWithResponse("select * from buys")
    except:
        print ("error when selecting all from buys")
        return []


def sellData():
    try:
        return database.runQueryWithResponse("select * from sells")
    except:
        print ("error when selecting all from sells")
        return []


def getStockCntByName(name):
    try:
        resBuy = database.runQueryWithResponse("select * from buys where stockname='"+name+"'")
        resSell = database.runQueryWithResponse("select * from sells where stockname='"+name+"'")
    except:
        print ("error")
        return 0
    cnt = 0
    
    for x in resBuy:
        cnt+= int(x[2])
    for x in resSell:
        cnt -= int(x[2])
    
    return cnt
    


