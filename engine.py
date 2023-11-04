import taipy as tp 
import landing_page as l_pg
'''
RUNNING IT ALL
'''
if __name__ == "__main__":
    tp.Gui(page = l_pg.landing_page,
           css_file='styling.css').run(use_reloader=True)

