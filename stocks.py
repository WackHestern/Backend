import database
import stockapi
import users
 
#return true if succeed 
def buy(stockName, amount):
    stockName=stockName.upper()
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
    stockName = stockName.upper()
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


def getStockCntByName(stockName):
    stockName = stockName.upper()
    try:
        resBuy = database.runQueryWithResponse("select * from buys where stockname='"+stockName+"'")
        resSell = database.runQueryWithResponse("select * from sells where stockname='"+stockName+"'")
    except:
        print ("error")
        return 0
    cnt = 0
    
    for x in resBuy:
        cnt+= int(x[2])
    for x in resSell:
        cnt -= int(x[2])
    
    return cnt
    
def canBuy(stockName, amount):
    price = float(stockapi.getPrice(stockName.upper()))
    
    availFunds = float(users.getAvailableFunds())
    
    cost= float(amount) * float(price)
    #make sure user has enough funds and update funds after buying
    if  cost > availFunds:
        return False
    return True
    
def canSell(stockName, amount):
    curStockCnt= int(getStockCntByName(stockName.upper()))
    amount = int(amount)
    if curStockCnt < amount:
        return False
    return True


def isValidName(stockName):
    return float(stockapi.getPrice(stockName.upper())) >= 0


def getCurrentList():
    buys = buyData()
    sells = sellData()
    ret = {} #key: stockName, value: amount
    
    tmp={}
    for b in buys:
        name = b[0]
        cnt = int(b[2])
        tmp[name] = tmp.get(name,0)+cnt
    
    for b in sells:
        name = b[0]
        cnt = int(b[2])
        tmp[name] = tmp.get(name,0)-cnt
    
    for k in tmp.keys():
        if tmp[k] >0:
            ret[k] = tmp[k]
    
    return ret



def getLastAdded():
    try:
        rBuy = database.runQueryWithResponse("select stockname, buyprice, amount, timestamp from buys order by timestamp desc limit 1;")
        rSell = database.runQueryWithResponse("select stockname, sellprice, amount, timestamp from sells order by timestamp desc limit 1;")

        print (rBuy)
        print (rSell)
        dateBuy = rBuy[3]
        dateSell = sBuy[3]
        print (dateBuy)
        print (dateSell)

        if dateSell < dateBuy:
            return {"stockName":rBuy[0], "price": rBuy[1], "amount": rBuy[2], "timestamp": rBuy[3], "action":"buy"}
        else:
            return {"stockName":rSell[0], "price": rSell[1], "amount": rSell[2], "timestamp": rSell[3], "action":"sell"}
        
    except Exception:
        print ("failed to get last added")
    return {}
        


def getPortfolioValue():
    stocks= getCurrentList()
    
    cnt=0.0
    
    for s in stocks:
        cnt += float(getStockCntByName(s)) * max(float(stockapi.getPrice(s)),0.0)
    
    return str(cnt)
    




