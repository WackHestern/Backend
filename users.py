import database
import stockapi


def getAvailableFunds():
    try:
        return database.runQueryWithResponse("select availableFunds from users where name='John Doe';")[0][0]
    except:
        return "-1"
    

#returns true if success
def updateFunds(newAmount):
    try:
        database.runQueryWithResponse("update users set availableFunds = '"+str(newAmount)+"' where name='John Doe';")
    except:
        return False
    
    
    return True
    
    