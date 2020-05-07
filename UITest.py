import tkinter as tkk
import webbrowser

def callback(url):
    webbrowser.open_new(url)

startingWindow = tkk.Tk()
startingWindow.title("Python Data WebScrapper")

frame_1 = tkk.Frame(startingWindow)
frame_2 = tkk.Frame(startingWindow)
frame_1.grid(row=0, column=0)
frame_2.grid(row=1, column=0)

# Labelframe
labelFrame1 = tkk.LabelFrame(frame_1, text="Please select the following options:", width=100)
labelFrame1.grid(row=0, column=1)

# first list
leagueSelect = tkk.Entry(labelFrame1, bd=5)
entryLabel3 = tkk.Label(labelFrame1, text="Select a League: ")
entryLabel3.grid(row=0, column=0)
leagueSelect.grid(row=0, column=1)


# second list
yearSel = tkk.Entry(labelFrame1, bd=5)
entryLabel = tkk.Label(labelFrame1, text="Select a year: ")
entryLabel.grid(row=0, column=2)
yearSel.grid(row=0, column=3)

# third  list
seasonSelct = tkk.Entry(labelFrame1, bd=5)
entryLabel2 = tkk.Label(labelFrame1, text="Select a season: ")
entryLabel2.grid(row=0, column=4)
seasonSelct.grid(row=0, column=5)

# Button
retrievePlayers = tkk.Button(frame_1, text="Retrieve Players", relief=tkk.RAISED, width=80)
retrievePlayers.grid(row=2, column=1)

# Canvas to start on
canvas = tkk.Canvas(frame_2, width=500, height=500, bg="Black")
canvas.grid(row=0)

#
ListBox = tkk.Listbox(canvas, width=100, height=30, bg="white")
ListBox.grid(row=0, column=1)


startingWindow.mainloop()
