from taipy import Gui
import config   # environment variables



# MAIN PAGE
home_page = """

#Getting Started with ***ByteBuy***

My text: <|{text}|>
<|{text}|input|>

"""



text = "Test Original test"



Gui(home_page).run(use_reloader=True)


