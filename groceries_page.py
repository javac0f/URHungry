import taipy as tp
import config   # environment variables

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





