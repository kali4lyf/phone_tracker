from tkinter import *
import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False, False)
root.configure(bg='#96BFFF')  # Background color to light blue
key="YOUR_OPENCAGE_API_KEY"

def track():
    enter_nb = entry.get()
    number = phonenumbers.parse(enter_nb)

    location = geocoder.description_for_number(number, 'en')
    country.config(text=location)

    service = carrier.name_for_number(number, 'en')
    sim.config(text=service)

    query = str(location)
    results = OpenCageGeocode(key).geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")

def open_map():
    webbrowser.open("mylocation.html")

# Logo placeholder (using a simple label for now, since images are not used)
Label(root, text="📍", font=("Arial", 48), bg="#96BFFF").place(x=160, y=30)  # Simple icon to represent the logo

heading = Label(root, text="Track Number", font='arial 20 bold', fg="#39281E", bg="#96BFFF")
heading.place(x=120, y=140)  # Track number text centered below the "logo"

# Input field for phone number
entry = StringVar()
enter_nb = Entry(root, textvariable=entry, width=17, justify='center', bd=0, font='arial 20', bg="#2C3541", fg="white")
enter_nb.place(x=90, y=200)

# Search button (using default Tkinter button instead of an image)
btn = Button(root, text="🔍", font=('Arial', 20), cursor='hand2', bg="#96BFFF", bd=0, command=track, activebackground="#ED8051")
btn.place(x=160, y=260)  # Search button centered

# Labels for displaying country and SIM info
country = Label(root, text="Country", bg='#96BFFF', fg='black', font='arial 14 bold')
country.place(x=55, y=320)

sim = Label(root, text="SIM", bg='#96BFFF', fg='black', font='arial 14 bold')
sim.place(x=255, y=320)

# Button for viewing location map
open_map_btn = Button(root, text="Location", width=10, cursor='hand2', bg="#EE8C62", bd=0, command=open_map, activebackground='#ED8051', font='arial 14 bold')
open_map_btn.place(x=140, y=370)

# Footer with Instagram-like text
insta_page = Label(root, text="@pythonagham", bg='#96BFFF', fg='black', font='arial 10 bold italic')
insta_page.place(x=135, y=550)

root.mainloop()
