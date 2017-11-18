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
    runQuery("CREATE TABLE IF NOT EXISTS buys (stockName varchar(48) NOT NULL,  buyPrice varchar(48) NOT NULL, amount INT NOT NULL, timestamp TIMESTAMP DEFAULT NOW(),enabled integer NOT NULL DEFAULT '1');")
    addTestData();

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
    runQuery("INSERT INTO buys (stockname, buyprice, amount) VALUES ('apple','120','2') ('apple','23','10') ('google','400','7')")
    

