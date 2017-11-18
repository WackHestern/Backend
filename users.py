import database
import stockapi


def getAvailableFunds(name):
    return database.runQueryWithResponse("select availableFunds from buys where name="+name+";")