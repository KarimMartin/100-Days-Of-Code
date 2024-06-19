import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()  # Gets info from the entry box in our GUI
        ytObject = YouTube(ytLink)  # Creates a variable that stores the Youtube link
        video = ytObject.streams.get_highest_resolution()  # Getting the linked video's highest resolution
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Link is invalid!", text_color="red")




# System settings using customtkinter documentation
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Creating the customtkinter window using the documentation
app = customtkinter.CTk()  # Initialises the GUI window
app.geometry("720x480")  # Setting the size of the window
app.title("YouTube Downloader")

# Adding the UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")  # Creating the textbox UI element to add a title
title.pack(padx=10, pady=10)  # Adding padding to the title to make it visible

# Creating the link input
url_var = tkinter.StringVar()  # Store info in entry box to the variable url_var
link = customtkinter.CTkEntry(app, width=400, height=20, textvariable=url_var)  # Setting up the entry box, text entered will be stored in url_var
link.pack()  # Used to show the entry box on the popup

# Finished downloading label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Creating the download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)  # Button has the text 'download', runs the startDownload command each time it's pressed
download.pack(padx=10, pady=10)




# Running the app using the customtkinter documentation
app.mainloop()

