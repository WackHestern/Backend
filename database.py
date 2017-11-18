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
    conn = getConn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS buys (stockName varchar(48) NOT NULL,  buyPrice varchar(48) NOT NULL,timestamp TIMESTAMP DEFAULT NOW(),enabled integer NOT NULL DEFAULT '1');")






