# Import from standard library
import logging
import random
import re

# Import from 3rd party libraries
from taipy.gui import Gui, notify

from pages import home_page, order_detail_page,order_page

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def error_too_many_requests(state):
    """Notify user that too many requests have been made."""
    notify(state, "error", "Too many requests. Please wait a few seconds before generating another text or image.")
    logging.info(f"Session request limit reached: {state.n_requests}")
    state.n_requests = 1


# Define functions
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
    state.orders = [(k, v) for k, v in state.all_store[state.store].items()]

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
    state.order_tweet = f"Select order {state.order_detail} with ID {state.order_id}."

    # Notify the user in console and in the GUI
    logging.info(
        f"Store selected: {state.order_detail}, {state.order_id}"
    )
    notify(state, "success", "Order created!")

def confirm_request_items(state):
    pass

def navigate_to_order(state):
    pass




# Variables
tweet = ""
order_tweet = ""
order_selected = None
order_id = ""
order_detail = ""
orders = []
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
stores = list(all_store.keys())

n_requests = 0

store = "store not chosen"

# Called whever there is a problem
def on_exception(state, function_name: str, ex: Exception):
    logging.error(f"Problem {ex} \nin {function_name}")
    notify(state, 'error', f"Problem {ex} \nin {function_name}")


# Markdown for the entire page
## <text|
## |text> 
## "text" here is just a name given to my part/my section
## it has no meaning in the code



root_md = """
<center>\n<|navbar|>\n</center>
## UR**Hungry**{: .color-secondary}
"""


page = """
<|container|

<br/>

<center><h3>Select from **store**{: .color-secondary}:</h3></center>

<center><|{store}|selector|lov={stores}|dropdown|></center>

<br/>

<center><|Show orders|button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{order_selected}|selector|lov={orders}|></center>

<center><|Show order selected|button|on_action=select_order|label=Show order selected|></center>

<center><|{order_tweet}|text|></center>

|>
"""





pages = {
    "/": root_md,
    "home":home_page,
    "order":page,
    "details": order_detail_page,
}

if __name__ == "__main__":
    Gui(pages=pages, css_file='./src/styling.css').run(title='Choose store')