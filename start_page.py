# Import from standard library
import logging
import random
import re

# Import from 3rd party libraries
from taipy.gui import Gui, notify

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def error_too_many_requests(state):
    """Notify user that too many requests have been made."""
    notify(state, "error", "Too many requests. Please wait a few seconds before generating another text or image.")
    logging.info(f"Session request limit reached: {state.n_requests}")
    state.n_requests = 1


# Define functions
def generate_text(state):
    """Generate Tweet text."""
    state.tweet = ""

    # Check the number of requests done by the user
    if state.n_requests >= 5:
        error_too_many_requests(state)
        return
    
    # Generate the tweet
    state.n_requests += 1
    state.tweet = f"Showing orders from {state.store}:"

    # Notify the user in console and in the GUI
    logging.info(
        f"Store selected: {state.tweet}"
    )
    notify(state, "success", "Order created!")


# Variables
tweet = ""
n_requests = 0

store = "Walmart"

# Called whever there is a problem
def on_exception(state, function_name: str, ex: Exception):
    logging.error(f"Problem {ex} \nin {function_name}")
    notify(state, 'error', f"Problem {ex} \nin {function_name}")


# Markdown for the entire page
## <text|
## |text> 
## "text" here is just a name given to my part/my section
## it has no meaning in the code
page = """
<|container|
# UR**Hungry**{: .color-secondary}

<br/>

<|layout|columns=1 1 1|gap=30px|class_name=card|

<store|
## Select from **store**{: .color-primary}:

<|{value}|selector|lov=Walmart;Target;Wegmans|dropdown|>
|store>

<|Show orders|button|on_action=generate_text|label=Show orders|>
|>

<br/>

### Show orders from **selected store**{: .color-primary}

<|{tweet}|input|multiline|label=Resulting tweet|class_name=fullwidth|>

|>
"""


if __name__ == "__main__":
    Gui(page).run(title='Tweet Generation')