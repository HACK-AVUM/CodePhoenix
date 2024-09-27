import dearpygui.dearpygui as dpg
import requests
from dearpygui.dearpygui import window


def save_callback(sender, app_data, user_data):
    print("Save button clicked!")
    data = {"message": "Data from GUI"}
    #response = requests.post("http://localhost:5000/api/data", json=data)
    #print(response.json())

def create_gui():
    dpg.create_context()
    dpg.create_viewport(title='AI-SYSTEM-Multi-Agent', width=1200, height=800)

    with dpg.window(label="Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save", callback=save_callback)
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    create_gui()
