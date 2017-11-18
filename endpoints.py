from flask import Flask, json, request
import database
import stocks
import users
import os

app = Flask(__name__)

# Post a json to flask server


@app.route('/test', methods=['Post', 'Get'])
def api_root():
    # validate that user sends in a json
    #if request.headers['Content-Type'] != 'application/json':
    #    return "Please post a JSON"

    #data = json.loads(json.dumps(request.json))

    # data is a map of all the json input

    # do whatever computation you want here

    # making something to return
    #returnThing = {'message': 'look its a message'}
    #return json.dumps(returnThing)
    
    database.addTestData()
    returnThing = {'message': 'adding test data to DB'}
    return json.dumps(returnThing)

@app.route('/stocks/buy', methods=['Post', 'Get'])
def buyStock():
    
    #if request.headers['Content-Type'] != 'application/json':
    #    return json.dumps({'message': 'invalid'})

    #data = json.loads(json.dumps(request.json))
    
    #if (stocks.buyStock(data["stockName"], data["amount"])):
    ret = stocks.buy("TSLA", 3)
    return json.dumps({'message': ret})
    #ret = success, fail, insufficient funds


@app.route('/stocks/sell', methods=['Post', 'Get'])
def sellStock():
    ret = stocks.sell("TSLA", 2)
    return json.dumps({'message': ret})
    #ret = success, fail, insufficient stocks


@app.route('/stocks/data', methods =['Post', 'Get'])
def getStockData():
    
    #t = database.runQueryWithResponse("select * from buys")
    
    ret = {'buyData': stocks.buyData(), 'sellData': stocks.sellData()}
    return json.dumps(ret)


@app.route('/user/availablefunds', methods =['Post', 'Get'])
def getUserAvailableFunds():
        
    ret = {'availableFunds': users.getAvailableFunds() }
    return json.dumps(ret)


@app.route('/stocks/cansell', methods=['Post', 'Get'])
def canSellStock():
    return json.dumps({"result": stocks.canSell("TSLA",2)})
    
@app.route('/stocks/canbuy', methods=['Post', 'Get'])
def canBuyStock():
    return json.dumps({"result": stocks.canBuy("TSLA",2)})



if __name__ == '__main__':
    database.initialize() 
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=True, host='0.0.0.0', port=port)
