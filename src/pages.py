#  markdown element of the pages
root_md="""
## UR**Hungry**{:.color-secondary}
<center>
<|navbar|lov={[("home", "Order"), ("trend","Trends"),("https://www.wegmans.com/", "Wegmans"),("https://www.walmart.com/", "Walmart"), ("https://www.yelp.com/menu/international-food-market-and-cafe-rochester-5", "International Food Market")]}|>
</center>
"""


home_page = """
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>Start ordering with friends **now**{: .color-secondary}!</h3></center>

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

<center><|{store}|label=store|selector|lov={stores_list}|dropdown|></center>

<br/>

<center><|Show orders|button|class_name = .taipy-button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{store_description}|text|></center>

<center><|{order_selected}|selector|lov={orders_list}|width=700|class_name=.taipy-selector|></center>

<br/>

<center><|Show Selectedd Shopping List|button|class_name = .taipy-button|on_action=select_order|label=Show order selected|></center>

<br/>

<center><|Create new Shopping List|button|class_name = .taipy-serious-button|on_action=create_new_order|label=Start new order|></center>

"""


order_detail_page = """

<br/>
<br/>

<center><h3>Add to **order**{: .color-secondary}:</h3></center>

<center><|{order_detail_description}|text|></center>

<br/>

<|layout|columns=1 1|gap=30px|class_name=card|

<|

<item_name|
<center><|{item_name}|input|label=Item name|></center>
|item_name>

<item_price|
<center><|{item_price}|input|label=Item price|></center>
|item_price>

<item_quantity|
<center><|{item_quantity}|input|label=Item quantity|></center>
|item_quantity>

<br/>

<center><|Add item|button|class_name = .taipy-button|on_action=add_item_to_order|label=Add item|></center>

|>

<|
<|{food_df}|table|columns={food_df.columns}|on_delete=food_df_on_delete|show_all|>

|>

|>

<br/>

<center><|Request items|button|class_name = .taipy-button|on_action=confirm_request_items|label=Request items|></center>

"""


trend_page = """
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>Inspecting the **trends**{: .color-secondary} around this neighborhood...</h3></center>


"""


order_success_page = """
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>Order **succeeded!**{: .color-secondary}</h3></center>

<center><|RETURN|button|class_name = .taipy-button|on_action=navigate_to_order|></center>\n



"""
