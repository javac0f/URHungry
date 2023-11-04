import taipy as tp
from taipy import Gui
from taipy.gui import Markdown, Html




user:str = "Josh"
product:str = "eggs"



home_page = """

<|container|
#**URHungry**


<|layout|columns=1|class_name=layout|


<h3 style="text-align: center;">{user} is ordering {product}{.:blue}</h3>

<center><|ORDER|button|class_name = .taipy-button|></center>\n

|>
|>

"""

