#  markdown element of the pages

root_md="## UR**Hungry**{:.color-secondary}"


home_page = """
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>Start ordering **now**{: .color-secondary}!</h3></center>

<center><|ORDER|button|class_name = .taipy-button|on_action=navigate_to_order|></center>\n

"""



order_page = """

<br/>
<br/>

<user_name|
<center><|{user_name}|input|label=Your name (or PseudoName)|></center>
|user_name>

<br/>

<center><h3>... is ordering from **store**{: .color-secondary}:</h3></center>

<center><|{store}|selector|lov={stores_list}|dropdown|></center>

<br/>

<center><|Show orders|button|class_name = .taipy-button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{store_description}|text|></center>

<center><|{order_selected}|selector|lov={orders_list}|></center>

<center><|Show order selected|button|class_name = .taipy-button|on_action=select_order|label=Show order selected|></center>

<br/>

<center><|Start new order|button|class_name = .taipy-serious-button|on_action=create_new_order|label=Start new order|></center>

"""

order_page_v2 = """

<br/>

<center><h3>Select from **STORE**{: .color-secondary}:</h3></center>

<center><|{store}|selector|lov={stores}|dropdown|></center>

<br/>

<center><|Show orders|button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{order_selected}|selector|dropdown=True|lov={orders}|></center>

<center><|Show order selected|button|on_action=select_order|label=Show order selected|></center>

<center><|{order_tweet}|text|></center>


"""





order_detail_page = """

<br/>
<br/>

<center><h3>Add to **order**{: .color-secondary}:</h3></center>

<br/>

<center><|{order_detail_description}|text|></center>

<br/>
<br/>

<|layout|columns=1 1 1|gap=30px|class_name=card|

<item_name|
<|{item_name}|input|label=Item name|>
|item_name>

<item_price|
<|{item_price}|input|label=Item price|>
|item_price>

<item_quantity|
<|{item_quantity}|input|label=Item quantity|>
|item_quantity>

|>

<br/>
<br/>

<center><|Add item|button|class_name = .taipy-button|on_action=add_item_to_order|label=Add item|></center>

<br/>
<br/>

<center><|Request items|button|class_name = .taipy-button|on_action=confirm_request_items|label=Request items|></center>

"""
