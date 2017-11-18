import database
import stockapi


def getAvailableFunds():
    try:
        return database.runQueryWithResponse("select availableFunds from users where name='John Doe';")[0][0]
    except Exception:
        return "-1"
    

#returns true if success
def updateFunds(newAmount):
    try:
        database.runQuery("update users set availableFunds = '"+str(newAmount)+"' where name='John Doe';")
    except Exception:
        return False
    
    
    return True
    
    