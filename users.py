import database
import stockapi


def getAvailableFunds(name):
    try:
        return database.runQueryWithResponse("select availableFunds from users where name='"+name+"';")[0]
    except:
        return "-1"