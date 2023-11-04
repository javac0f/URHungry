import taipy as tp




landing_page = """

<|container|

# **ByteBuy**
<br/>


<|layout|columns = 1| gap = 100 px | class_name = card|

<order|
<center><|None|button|label=Order an Item|></center>
|order>


<connect|
<center><|None|button|label=Connect to Others Nearby|></center>
|connect>

<about|
<center><|ABOUT|button|label=Our Story|></center>
|about>


<br/>

---

<br/>

###



|>
"""

grocery_page = """

        #*Input Grocery*

        <|"Grocery:"|input|>
        <|submit|button|on_action=submit_scenario|>



"""




def on_button_action(state):
    tp.notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
    
def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = tp.scenario.message.read()

