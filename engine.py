import taipy as tp 
imoprt pages





menu_layout = {
    "/": "<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "HOME": pages.landing_page,
    "STATS": pages.landing_page,
    "ABOUT": pages.landing_page,
}


if __name__ == "__main__":
    tp.Gui(pages = menu_layout,
           css_file='styling.css').run(use_reloader=True)

