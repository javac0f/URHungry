root_md="## UR**Hungry**{:.color-secondary}"


home_page = """
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>**Josh**{:.color-secondary} is ordering from **Wegmans**{:.color-secondary}</h3></center>

<center><|ORDER|button|class_name = .taipy-button|on_action=navigate_to_order|></center>\n

"""



order_page = """

<br/>
<br/>
<center><h3>Select from **store**{: .color-secondary}:</h3></center>

<center><|{store}|selector|lov={stores_list}|dropdown|></center>

<br/>

<center><|Show orders|button|class_name = .taipy-button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{order_selected}|selector|lov={orders_list}|></center>

<center><|Show order selected|button|class_name = .taipy-button|on_action=select_order|label=Show order selected|></center>

<center><|{order_tweet}|text|></center>

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

<center><|Request items|button|class_name = .taipy-button|on_action=confirm_request_items|label=Request items|></center>

"""
