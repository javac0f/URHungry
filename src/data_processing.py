#  structure of the data

from hedera import PrivateKey
prikey = PrivateKey.generate()
print("Private key: {}".format(prikey.toString()))
print("Public key: {}".format(prikey.getPublicKey().toString()))



payment = {
    "card_number" : "1252 2251 2654 1253", # primary key
    "expiry_date" : "07/25",
    "CVV/CVC" : "000",
}

user = {
    "user_id" : 1234, # primary key
    "user_name" : "luna",
    "payment" : payment,
    "preferred_location" : "southside",
}

item = {
    "name" : "potato",
    "quantity" : 3,
    "quote_price" : 3.5, # in dollars
    ""
}

order = {
    "id" : 1154, # primary key
    "order_id" : 1254656,
    "user_id" : 1234,
    "store" : "walmart", # store to order from
    "item" : item,
    "delivery_by_date" : "12/05/2023", # the date by which the order must arrive
}


def pull_order(store, by_date, *orders):
    """
    store: the store chosen by the user
    by_date: 
    orders: a list of orders from the database
    """
    chosen = []
    for order in orders:
        if order["store"] == store and order["date"].later(by_date):
            chosen.append(order)
    return chosen
    

def order_summary(orders):
    display 
    for order in orders:
        order
