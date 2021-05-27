#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time, cbpro

wsc = cbpro.WebsocketClient(url="wss://ws-feed.pro.coinbase.com",
                                products="ADA-USD",
                                channels=["ticker"])


# In[ ]:


class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["ETH-USDT"]
        self.channels=["ticker"]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("Closing")

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products, wsClient.channels)
while (wsClient.message_count < 50):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(1)
wsClient.close()

