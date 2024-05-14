import tkinter as tk  # Import standard tkinter for Listbox and IntVar
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from turtledemo.__main__ import font_sizes

from customtkinter import CTkFont


class MainPageGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Selection Robot")
        self.root.geometry("700x350+100+100")  # Window size and position
        self.setup_ui()

    def setup_ui(self):
        base_width = 800

        self.city_combo = ttk.Combobox(self.root, values=["Beijing", "Chicago", "Dubai", "Las Vegas", "London", "Montreal", "New Delhi", "New York City", "San Francisco", "Shanghai"], state='readonly', width=20)
        self.city_combo.set("Beijing")
        self.city_combo.place(x=30, y=10)

        search_button = ttk.Button(self.root, text="Search", width=50)
        search_button.place(x=200, y=10)

        # Center Section for checkboxes
        frame_center = ttk.Frame(self.root, height=250, width=140)
        frame_center.place(x=0, y=60)

        attributes = ["Cleanliness", "Room", "Service", "Location", "Value", "Safety", "Comfort", "Transportation", "Noise"]
        self.vars = []
        checkbox_y = 10
        for attribute in attributes:
            var = tk.IntVar()  # Use standard IntVar
            checkbox = ttk.Checkbutton(frame_center, text=attribute, variable=var, command=lambda v=var: self.check_limit(v), width=200)
            checkbox.place(x=10, y=checkbox_y)
            checkbox_y += 35
            self.vars.append(var)

        sample_hotels = [
            "Hotel California", "Grand Plaza Resort", "Ocean View Inn", "Mountain Retreat Hotel",
            "Urban Boutique Hotel", "Cozy Cottage B&B", "Luxury City Center Suite", "Airport Gateway Hotel",
            "Beachside Bungalow", "Historic Downtown Hostel", "Skyline Tower Suites", "Riverside Grand Hotel",
            "Cityscape Luxury Apartments", "Golden Horizon Villas", "Silver Sands Resort", "Oasis Palm Hotel",
            "Blue Lagoon Getaway", "Starlight Boutique Hotel", "Harmony Retreat and Spa", "Sunset Marina Resort",
            "Crystal Lake Cabins", "Regal Manor Inn", "Imperial Garden Hotel", "Metropolitan Park Hotel",
            "Whispering Pines Lodging", "Coral Beach Hotel", "Rainforest Eco-Lodge", "Gateway Urban Hotel",
            "Continental Suites", "Sapphire Bay Resort", "Hilltop Heritage Inn", "Tranquil Nights B&B",
            "Emerald City Hotel", "Royal Oak Resort & Spa", "Highland Mountain Resort"
        ]

        frame_list = ttk.Frame(self.root, height=250, width=int(base_width / 2))
        frame_list.place(x=150, y=60)

        self.listbox = tk.Listbox(frame_list, width=50, height=13, font='Arial')
        self.listbox.place(x=10, y=10)

        # Insert sample data into the listbox
        sample_hotels = ["Hotel California", "Grand Plaza Resort", "Ocean View Inn", "Mountain Retreat Hotel",
                         "Urban Boutique Hotel", "Cozy Cottage B&B", "Luxury City Center Suite",
                         "Airport Gateway Hotel", "Beachside Bungalow", "Historic Downtown Hostel"]

        for hotel in sample_hotels:
            self.listbox.insert(tk.END, hotel)



    def check_limit(self, current_var):
        # Count how many checkboxes are checked
        count = sum(v.get() for v in self.vars)
        if count > 3:
            current_var.set(0)  # Uncheck the box if the limit is exceeded

# Create the main window and pass it to the MainPageGUI class
root = tk.Tk()
app = MainPageGUI(root)
root.mainloop()
