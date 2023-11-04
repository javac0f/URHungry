from taipy import Gui
from pages import home_page, orderby_page



if __name__ == "__main__":
    #Core().run()
    #scenario = tp.create_scenario(scenario_cfg)
    Gui(page = home_page, css_file = './styling.css').run(use_reloader=True)

