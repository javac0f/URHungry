home_page = """

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<center><h3>**Josh**{:.color-secondary} is ordering from **Wegmans**{:.color-secondary}</h3></center>

<center><|ORDER|button|class_name = .taipy-button|on_action=nagivate_to_order|></center>\n

"""



order_page = """

<br/>
<br/>

<center><h3>Select from **store**{: .color-secondary}:</h3></center>

<center><|{store}|selector|lov={stores}|dropdown|></center>

<br/>

<center><|Show orders|button|class_name = .taipy-button|on_action=choose_store|label=Show orders|></center>

<br/>

<center><|{order_selected}|selector|lov={orders}|></center>

<center><|Show order selected|button|class_name = .taipy-button|on_action=select_order|label=Show order selected|></center>

<center><|{order_tweet}|text|></center>

"""
