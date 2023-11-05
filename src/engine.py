# Import from standard library
import logging
import random
import re
import pandas as pd

# Import from 3rd party libraries
from taipy.gui import Gui, notify, navigate

# Import pages
import pages 







# HOME PAGE FUNCTIONS

def navigate_to_order(state):
    navigate(state, "order")


# ORDER PAGE FUNCTIONS

# Handling data
stores_df = pd.read_csv("database/stores.csv", index_col="StoreName")
stores_list = list(stores_df.index)

orders_df = pd.read_csv("database/orders.csv", index_col="ID")
items_df = pd.read_csv("database/items.csv", index_col="ID")


# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

MAX_REQUEST = 20

def error_too_many_requests(state):
    """Notify user that too many requests have been made."""
    notify(state, "error", "Too many requests. Please wait a few seconds before generating another text or image.")
    logging.info(f"Session request limit reached: {state.n_requests}")
    state.n_requests = 1


# Define functions
def sort_by_date_store(store, sort_by_date=True):
    orders = orders_df

    print(orders)

    # check if the store requested even have any order:
    if store not in list(orders["StoreName"]):
        return []

    # get all order with this store name 
    orders = orders[orders["StoreName"] == store]
    items = items_df.copy()
    items["Total"] = items["Price"]*items["Quantity"]
    orders["MinOrder"] = stores_df["MinOrder"][store]

    # join order table with the sum based on order ID 
    orders["Total"] = items.groupby('OrderID').sum()["Total"]
    orders["Percentage"] = orders["Total"]/orders["MinOrder"]*100
    orders["Completion"] = orders["Percentage"].apply(lambda x: 100 if x > 100 else x)
    orders["Descriptor"] = [f"{date} - {int(comp)}%" for date, comp in zip(orders["OrderDate"], orders["Completion"])]
    # orders.apply(lambda x: f"{x['OrderDate']} {x['Completion']}%")
    return [(id, desc) for id, desc in zip(orders.index, orders["Descriptor"])]


def get_order_total(order_id):
    this_order = items_df[items_df["OrderID"] == order_id]
    this_order["Total"] = this_order["Price"]*this_order["Quantity"]

    return sum(this_order["Total"])

# choose store button
def choose_store(state):
    # Check the number of requests done by the user
    if state.n_requests >= MAX_REQUEST:
        error_too_many_requests(state)
        return
    
    # Check if the user has put a store name
    if state.store == "":
        notify(state, "error", "Please select a store")
        return

    # Generate the order list
    state.n_requests += 1
    state.orders_list = sort_by_date_store(store=state.store)

    if len(state.orders_list) > 0:
        state.store_description = f"Showing active orders from {state.store}:"
    else:
        state.store_description = f"There are no current active order at this store. Please place a new order."


    # Notify the user in console and in the GUI
    logging.info(
        f"Store selected: {state.store}"
    )
    notify(state, "success", "Store selected!")


def create_new_order(state):
    # Check if the user has put a name
    if state.user_name == "":
        notify(state, "error", "Please enter a name")
        return

    # Check the number of requests done by the user
    if state.n_requests >= MAX_REQUEST:
        error_too_many_requests(state)
        return
    
    # generate new id for order 
    state.order_id = int(orders_df.index[-1]) + 1

    # get info of this order to pass to next page
    state.current_order_price = 0
    state.min_price = stores_df.loc[state.store]["MinOrder"]
    if state.min_price < 1:
        state.min_price = 0
    state.more_money = state.min_price

    # set up the description for next page 
    state.order_detail_description = f"Order is at ${state.current_order_price}. Order needs ${state.more_money} to reach the minimum order price of ${state.min_price}."


    # Notify the user in console and in the GUI
    logging.info(
        f"Creating new order with ID {state.order_id}."
    )
    notify(state, "success", "Order created!")

    navigate(state, "order_detail")


def select_order(state):
    # Check if the user has put a name
    if state.user_name == "":
        notify(state, "error", "Please enter a name")
        return

    # Check if the user has selected an order
    if state.order_selected == None:
        notify(state, "error", "Please enter a name")
        return

    # Check the number of requests done by the user
    if state.n_requests >= MAX_REQUEST:
        error_too_many_requests(state)
        return
    
    # Select the order
    state.n_requests += 1
    state.order_id = state.order_selected[0]
    state.order_detail = state.order_selected[1]

    # get info of this order to pass to next page
    state.current_order_price = get_order_total(state.order_id)
    print(get_order_total(state.order_id))
    state.min_price = stores_df.loc[state.store]["MinOrder"]
    if state.min_price < 1:
        state.min_price = 0

    # check amount of money needed to reach minimum order 
    state.more_money = state.min_price - state.current_order_price
    if state.more_money <= 0:
        state.more_money = 0

    # set up the description for next page 
    state.order_detail_description = f"Order is at ${state.current_order_price}. Order needs ${state.more_money} to reach the minimum order price of ${state.min_price}."

    # Notify the user in console and in the GUI
    logging.info(
        f"Select order {state.order_detail} with ID {state.order_id}."
    )
    notify(state, "success", "Order created!")

    navigate(state, "order_detail")


# Variables
user_name = ""

store_description = ""
order_selected = None
order_id = ""
order_detail = ""
orders_list = []

current_order_price = 0
more_money = 0
min_price = 0
order_detail_description = ""

n_requests = 0

store = "store not chosen"

# Called whever there is a problem
def on_exception(state, function_name: str, ex: Exception):
    logging.error(f"Problem {ex} \nin {function_name}")
    notify(state, 'error', f"Problem {ex} \nin {function_name}")



# ORDER DETAIL PAGE
item_name = ""
item_price = ""
item_quantity = ""

new_item_list = []
new_item_list_dropdown = []

food_df = pd.DataFrame({
    "Item" : [],
    "Price" : [],
    "Quantity" : [],
})

item_delete_selected = None

def food_df_on_delete(state, var_name, payload):
    index = payload["index"] # row index
 
    state.food_df = state.food_df.drop(index=index)
    notify(state, "success", f"Item is deleted!")

def append_item(new_item_list):
    # items_df.loc[len(items_df.index)+1] = new_item_list
    # items_df.append
    items_df = items_df.append(pd.DataFrame([new_item], columns=items_df.columns), ignore_index=True)


def add_item_to_order(state):
    # check if empty:
    if state.item_name == "" or state.item_price == "" or state.item_quantity == "":
        notify(state, "error", "Please enter all the fields needed.")
        return

    state.n_requests += 1

    # New list for append into DataFrame
    # new_item = {
    #     "User" : state.user_name, 
    #     "Name" : state.item_name, 
    #     "Price" : state.item_price, 
    #     "Quantity" : state.item_quantity, 
    #     "OrderID" : state.order_id,
    # }

    new_item = [
        state.user_name, 
        state.item_name, 
        state.item_price, 
        state.item_quantity, 
        state.order_id,
    ]

    new_item_descriptor = f"{state.item_name} at ${state.item_price} x{state.item_quantity}"

    new_row = pd.DataFrame({
        "Item" : [state.item_name],
        "Price" : [state.item_price],
        "Quantity" : [state.item_quantity],
    })
    state.food_df = pd.concat([new_row, state.food_df], axis=0, ignore_index=True)

    # Using append to add the list to DataFrame
    state.new_item_list.append(new_item)
    state.new_item_list_dropdown.append((0, new_item_descriptor))
    
    state.item_name = ""
    state.item_price = ""
    state.item_quantity = ""

    # Notify the user in console and in the GUI
    logging.info(
        new_item_list_dropdown
    )
    notify(state, "success", "New item added!")


def delete_item_from_order(state):
    # Check if the user has selected an order
    if state.item_delete_selected == None:
        notify(state, "error", "Please select an item to delete")
        return

    # Select the order
    state.n_requests += 1

    delete_index = state.new_item_list_dropdown.index(state.item_delete_selected)
    del state.new_item_list_dropdown[delete_index]
    del state.new_item_list[delete_index]

    # Notify the user in console and in the GUI
    logging.info(
        state.new_item_list
    )
    notify(state, "success", "Selected item deleted!")


def confirm_request_items(state):
    # check if empty
    if len(state.food_df) == 0:
        notify(state, "error", "Please add at least 1 item.")
        return

    # append_item(state.new_item_list)

    # print(items_df)

    # Notify the user in console and in the GUI
    logging.info(
        state.new_item_list
    )
    notify(state, "success", "Succeeded in adding items!")

    navigate(state, "order_success")




# PAGES NAVIGATION

pages = {
    "/": pages.root_md,
    "home": pages.home_page,
    "order": pages.order_page,
    "order_detail": pages.order_detail_page,
    "order_success": pages.order_success_page,
    "trend": pages.trend_page
}

stylekit = {
    "color_primary": "#E5CCFF",
    "color_secondary": "#C0FFE",
    "color-paper-dark": "#1b002b",
    "color-background-dark": "#1B002C",
}

if __name__ == "__main__":
    #Core().run()
    #scenario = tp.create_scenario(scenario_cfg)
    Gui(pages=pages, css_file = './styling.css').run(use_reloader=True, title='URHungry',stylekit=stylekit)

