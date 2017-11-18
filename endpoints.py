from flask import Flask, json, request
import database.py 
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
    returnThing = {'message': 'look its a message'}
    return json.dumps(returnThing)

@app.route('/stocks/buy', methods=['Post', 'Get'])
def buyStock():
    ret = {'message': 'buy stock is not implemented yet'}
    return json.dumps(ret)


@app.route('/stocks/sell', methods=['Post', 'Get'])
def sellStock():
    ret = {'message': 'sell stock is not implemented yet'}
    return json.dumps(ret)


@app.route('/stocks/data', methods =['Post', 'Get'])
def getStockData():
    ret = {'message': 'get stock data not implemented'}
    return json.dumps(ret)


if __name__ == '__main__':
    database.initialize() 
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=True, host='0.0.0.0', port=port)
