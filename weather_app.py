import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
# from weather_api import weather_information

app = tk.Tk()
canvas = tk.Canvas(app, height = 600, width = 700)
canvas.pack()
app.resizable(False, False)
app.title("Weather-App")
# Code to add widgets will go here...

#set background image 
background_img = tk.PhotoImage(file="background-image.png")
background_label = tk.Label(app, image=background_img)
background_label.place(relwidth=1, relheight=1)

#heading of the app 
heading = tk.Label(app, 
                    text="Weather Information",
                    font=('Helvetica', 25, 'bold'),
                    bg="black",
                    fg="yellow",
                    bd=5,
                    pady=10
                    )
heading.place(relwidth=1)

#frame
frame = tk.Frame(app, bg='yellow', bd=5)
frame.place(x=100, y=80, relwidth=0.75, relheight=0.1)

# text-box
textbox = tk.Entry(frame, font=('Courier', 16, 'bold'), insertbackground='red', selectbackground='blue')
textbox.place(relwidth=0.65, relheight=1)

#submit button
submit_btn = tk.Button(frame,
                        text="Search Weather",
                        font=35,
                        cursor='hand2'
                            
                            )
submit_btn.place(x=360, relwidth=0.3, relheight=1)

#information frame 
info_frame = tk.Frame(app, bg='yellow', bd=6)
info_frame.place(x=100, y=200, relwidth=0.75, relheight=.55)

result = tk.Label(info_frame, text="Weather Information", font=('Courier', 16), anchor='n', justify='center', bg='white', pady=15)
result.place(relwidth= 1, relheight = 1)

#Canvas for weather icon
weather_icon = tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0,relwidth=1, relheight=.5)


app.mainloop()