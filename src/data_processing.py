#  structure of the data

payment = {
    "card_number" : "1252 2251 2654 1253", # primary key
    "expiry_date" : "07/25",
    "CVV/CVC" : "000",
}

store = {
    "name" : "walmart", # primary key
    "min_order" : 35.00, # in dollars
    "min_order_fee" : 7.95,
    "fees" : 7.85,
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
    "alternatives" : [],
}

order = {
    "order_id" : 1254656,
    "opener" : "John Doe",
    "public" : False,
    "date" : "12/05/2023", # (iterable) date on which the order arrive
}

items = {
    "id" : 1154, # primary key
    "order" : order,
    "user_id" : 1234,
    "store" : store, # store to order from
    "item" : item,
}

def pull_order_by_store(store, orders):
    """
    store: the store chosen by the user
    orders: a list of orders from the database
    """
    chosen = {}
    for order in orders:
        if order["store"] == store:
            chosen.update(order, order["order"]["date"])
    return sorted(chosen)    

def pull_order(stores, orders):
    """
    stores: all stores are that can be requested
    orders: a list of orders from the database
    """
    chosen = {}
    for store in stores:
        chosen.update(store, pull_order_by_store(store, orders)) 
    return chosen

def order_summary(orders):
    # the orders have the same store
    tax_rate = 0.08
    display = {
        "subtotal" : 0,
        "taxes and fees" : 0,
    }
    subtotal = 0
    for order in orders:
        item = order["item"]
        subtotal += (item["quantity"]*item["quote_price"])
    display["subtotal"] = subtotal
    store = order[0]["store"]
    fees = store["fees"]
    if subtotal < store["min_order"]:
        fees += store["min_order_fee"]
    taxes_and_fees = subtotal*tax_rate
    display["taxes and fees"] = taxes_and_fees
    return display


def list_items(orders):
    items = [orders["item"]]
    return [{
        "item_name" : items["name"],
        "quantity" : items["quantity"],
    }]


data = 