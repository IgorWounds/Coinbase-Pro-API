import cbpro
import base64
import json
from time import sleep

key = ''
secret = ''
passphrase = ''

encoded = json.dumps(secret).encode()
b64secret = base64.b64encode(encoded)
auth_client = cbpro.AuthenticatedClient(key=key, b64secret=secret, passphrase=passphrase)
c = cbpro.PublicClient()

while True:
    try:
        ticker = c.get_product_ticker(product_id='BTC-USD')
    except Exception as e:
        print(f'Error obtaining ticker data: {e}')
    
    if float(ticker['price']) >= 38500.00:
        try:
            limit = c.get_product_ticker(product_id='ETH-USD')
        except Exception as e:
            print(f'Error obtaining ticker data: {e}')
        
        try:
            order=auth_client.place_limit_order(product_id='ETH-USDT', 
                              side='buy', 
                              price=float(limit['price'])+2, 
                              size='0.007')
        except Exception as e:
            print(f'Error placing order: {e}')
        
        sleep(2)
        
        try:
            check = order['id']
            check_order = auth_client.get_order(order_id=check)
        except Exception as e:
            print(f'Unable to check order. It might be rejected. {e}')
        
        if check_order['status'] == 'done':
            print('Order placed successfully')
            print(check_order)
            break
        else:
            print('Order was not matched')
            break
    else:
        print(f'The requirement is not reached. The ticker price is at {ticker["price"]}')
        sleep(10)
