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

def nagivate_to_order(state):
    navigate(state, "order")







# ORDER PAGE FUNCTIONS

# Handling data
stores_df = pd.read_csv("database/stores.csv", index_col="StoreName")
stores_list = list(stores_df.index)

orders_df = pd.read_csv("database/orders.csv", index_col="ID")
items_df = pd.read_csv("database/items.csv", index_col="ID")


# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def error_too_many_requests(state):
    """Notify user that too many requests have been made."""
    notify(state, "error", "Too many requests. Please wait a few seconds before generating another text or image.")
    logging.info(f"Session request limit reached: {state.n_requests}")
    state.n_requests = 1


# Define functions
def sort_by_date_store(store, sort_by_date=True):
    orders = orders_df
    orders = orders[orders["StoreName"] == store]
    items = items_df
    items["Total"] = items["Price"]*items["Quantity"]
    orders["MinOrder"] = stores_df["MinOrder"][store]
    orders["Total"] = items.groupby('OrderID').sum()["Total"]
    orders["Percentage"] = orders["Total"]/orders["MinOrder"]*100
    orders["Completion"] = orders["Percentage"].apply(lambda x: 100 if x > 100 else x)
    orders["Descriptor"] = [f"{date} - {int(comp)}%" for date, comp in zip(orders["OrderDate"], orders["Completion"])]
    # orders.apply(lambda x: f"{x['OrderDate']} {x['Completion']}%")
    return [(id, desc) for id, desc in zip(orders.index, orders["Descriptor"])]


def choose_store(state):
    """Generate Tweet text."""
    state.tweet = ""

    # Check the number of requests done by the user
    if state.n_requests >= 5:
        error_too_many_requests(state)
        return
    
    # Generate the tweet
    state.n_requests += 1
    state.tweet = f"<h3>Showing orders from {state.store}:</h3>"
    state.orders_list = sort_by_date_store(store=state.store)

    # Notify the user in console and in the GUI
    logging.info(
        state.all_store[state.store],f"Store selected: {state.store}"
    )
    notify(state, "success", "Order created!")


def select_order(state):
    # Check the number of requests done by the user
    if state.n_requests >= 5:
        error_too_many_requests(state)
        return
    
    # Select the order
    state.n_requests += 1
    state.order_id = state.order_selected[0]
    state.order_detail = state.order_selected[1]

    # Notify the user in console and in the GUI
    logging.info(
        f"Select order {state.order_detail} with ID {state.order_id}."
    )
    notify(state, "success", "Order created!")

    navigate(state, "order_detail")


# Variables
tweet = ""
order_tweet = ""
order_selected = None
order_id = ""
order_detail = ""
orders_list = []
all_store = {
    "Wegmans": {
        "2332": "October 31 - 100%",
        "2739": "October 21 - 26%"
    },
    "Target": {
        "4788": "October 23 - 100%",
        "4272": "October 15 - 26%"
    },
    "Walmart": {
        "7020": "October 20 - 100%",
        "7292": "October 11 - 26%"
    },
}

n_requests = 0

store = "store not chosen"

# Called whever there is a problem
def on_exception(state, function_name: str, ex: Exception):
    logging.error(f"Problem {ex} \nin {function_name}")
    notify(state, 'error', f"Problem {ex} \nin {function_name}")









# PAGES NAVIGATION

pages = {
    "/": pages.root_md,
    "home": pages.home_page,
    "order": pages.order_page,
    "order_detail": pages.order_detail_page
}

if __name__ == "__main__":
    #Core().run()
    #scenario = tp.create_scenario(scenario_cfg)
    Gui(pages=pages, css_file = './styling.css').run(use_reloader=True)

