import websocket, json, time
#connects to coinbase websocket, creates socket object
cc = websocket.create_connection('wss://ws-feed.pro.coinbase.com')

#sends server a message in a string json form
cc.send(json.dumps({'type':'subscribe','product_ids':['BTC-USD']}))
#intial time/counter
t0 = time.time()
count = 0
while True:
    #received data is json'd 
    data = json.loads(cc.recv())
    #measuring the number of messages per second for latency testing
    if time.time() - t0 > 1:
        print('Messages per second: {}'.format(count))
        count = 0
        t0 = time.time()
    count += 1
    

