#  structure of the data

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

order = {
    "id" : 1154, # primary key
    "order_id" : 1254656,
    "user_id" : 1234,
    "store" : "walmart", # store to order from
    "item" : "potato",
    "delivery_by_date" : "12/05/2023", # the date by which the order must arrive
}

