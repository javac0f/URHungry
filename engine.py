import taipy as tp 
import pages





menu_layout = {
    
    "HOME": pages.landing_page,
    "STATS": pages.landing_page,
    "ABOUT": pages.landing_page,
}

stylekit = {
  "color_primary": "#BADA55",
  "color_secondary": "#C0FFE",
}


if __name__ == "__main__":
    tp.Gui(pages = menu_layout, css_file='./STYLES/styling.css').run(use_reloader=True)
