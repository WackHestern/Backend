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
    
    #if not request.headers or request.headers['Content-Type'] != 'application/json':
    #    return json.dumps({'message': 'invalid post'})

    data = json.loads(json.dumps(request.json))
    
    ret = stocks.buy(data["stockName"], data["amount"])
    return json.dumps({'message': ret})
    #ret = success, fail, insufficient funds


@app.route('/stocks/sell', methods=['Post', 'Get'])
def sellStock():
    if not request.headers or request.headers['Content-Type'] != 'application/json':
        return json.dumps({'message': 'invalid post'})

    data = json.loads(json.dumps(request.json))
    
    ret = stocks.sell(data["stockName"], data["amount"])
    return json.dumps({'message': ret})
    #ret = success, fail, insufficient stocks


@app.route('/stocks/data', methods =['Post', 'Get'])
def getStockData():
    ret = {'buyData': stocks.buyData(), 'sellData': stocks.sellData()}
    return json.dumps(ret)


@app.route('/user/availablefunds', methods =['Post', 'Get'])
def getUserAvailableFunds():        
    ret = {'availableFunds': users.getAvailableFunds() }
    return json.dumps(ret)


@app.route('/user/setfunds', methods = ['Post', 'Get'])
def setUserFunds():
    if not request.headers or request.headers['Content-Type'] != 'application/json':
        return json.dumps({'message': 'invalid post'})

    data = json.loads(json.dumps(request.json))
    
    if users.updateFunds(data["amount"]):
        return json.dumps({'message': 'success'})
    return json.dumps({'message': 'fail'})
    
    
    

@app.route('/stocks/cansell', methods=['Post', 'Get'])
def canSellStock():
    if not request.headers or request.headers['Content-Type'] != 'application/json':
        return json.dumps({'message': 'invalid post'})

    data = json.loads(json.dumps(request.json))
    
    return json.dumps({"result": stocks.canSell(data["stockName"], data["amount"])})
    
    

@app.route('/stocks/canbuy', methods=['Post', 'Get'])
def canBuyStock():
    if not request.headers or request.headers['Content-Type'] != 'application/json':
        return json.dumps({'message': 'invalid post'})

    data = json.loads(json.dumps(request.json))
    return json.dumps({"result": stocks.canBuy(data["stockName"], data["amount"])})


if __name__ == '__main__':
    database.initialize() 
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=True, host='0.0.0.0', port=port)
    
    

