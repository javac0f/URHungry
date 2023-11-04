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
    "id" : 1154, # primary key
    "order_id" : 1254656,
    "user_id" : 1234,
    "store" : store, # store to order from
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


