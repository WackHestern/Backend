import os
from urllib import parse 
import psycopg2

def getConn():
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn 

def initialize():
    #table to store current buys
    runQuery("CREATE TABLE IF NOT EXISTS buys (stockName varchar(48) NOT NULL, buyPrice varchar(48) NOT NULL, amount INT NOT NULL, timestamp TIMESTAMP DEFAULT NOW());")
    
    #table to store sells 
    runQuery("CREATE TABLE IF NOT EXISTS sells (stockName varchar(48) NOT NULL, sellPrice varchar(48) NOT NULL, amount INT NOT NULL, timestamp TIMESTAMP DEFAULT NOW());")
    
    runQuery("CREATE TABLE IF NOT EXISTS users (name varchar(48) NOT NULL, availableFunds varchar(48) NOT NULL);")
    
def runQuery(q):
    conn = getConn()
    cur = conn.cursor()
    
    cur.execute(q)

    conn.commit()
    cur.close()
    conn.close()

def runQueryWithResponse(q):
    conn = getConn()
    cur = conn.cursor()
    
    cur.execute(q)
    ret = cur.fetchall()
    
    conn.commit()
    cur.close()
    conn.close()
    
    return ret

def addTestData():
    runQuery("INSERT INTO buys (stockname, buyprice, amount, timestamp) VALUES ('AAPL','120',2,'2017-11-13 18:25:31.030608')")
    runQuery("INSERT INTO buys (stockname, buyprice, amount, timestamp) VALUES ('GOOGL','400',7, '2017-11-14 18:25:31.030608')")
    runQuery("INSERT INTO buys (stockname, buyprice, amount, timestamp) VALUES ('TSLA','23',10, '2017-11-16 18:25:31.030608')")
    runQuery("INSERT INTO users (name, availablefunds) VALUES ('John Doe','5000.34')")

