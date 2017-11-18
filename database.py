import os
from urllib import parse 
import psycopg2

def getConn():
    urlparse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["postgres://norlxajvyplpfe:e24415b89946199f789e67bf4538d4cd9ff9a12c53c4f1a7baeace48e029429e@ec2-23-23-249-169.compute-1.amazonaws.com:5432/d7npj38pkmgv9n"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )


def initialize():
    conn = getConn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS buys (stockName varchar(48) NOT NULL,  buyPrice varchar(48) NOT NULL,timestamp TIMESTAMP DEFAULT NOW(),enabled integer NOT NULL DEFAULT '1')")






