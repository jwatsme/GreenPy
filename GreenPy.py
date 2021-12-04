import tkinter as tk
window = tk.Tk()

#functions
def openOptionsWindow():
    optionsWindow = tk.Toplevel(window)
    optionsWindow.title("System Options")
    optionsWindow.geometry("200x200")
    tk.Label(optionsWindow, text = "System Options").pack()

def openPlantsWindow():
    plantsWindow = tk.Toplevel(window)
    plantsWindow.title("Plant Choice")
    plantsWindow.geometry("200x200")
    tk.Label(plantsWindow, text = "Plant Selector").pack()

def openEnvironmentWindow():
    environmentWindow = tk.Toplevel(window)
    environmentWindow.title("Environmental Parameters")
    environmentWindow.geometry("200x200")
    tk.Label(environmentWindow, text = "Environmental Parameters").pack()

#titles
window.title("GreenPy")

#labels
lblTitle = tk.Label(
    text = "GreenPy",
    fg = "white",
    bg = "#3CD812",
    width = 70,
    height = 5,
)

lblTime = tk.Label(
    text = "00:00",
    fg = "white",
    bg = "#3CD812",
    width = 15,
    height = 2,
)

lblDate = tk.Label(
    text = "00/00/00",
    fg = "white",
    bg = "#3CD812",
    width = 15,
    height = 2,
)

lblTemperature = tk.Label(
    text = "Temperature",
    fg = "white",
    bg = "#3CD812",
    width = 35,
    height = 2,
)

lblHumidity = tk.Label(
    text = "Humidity",
    fg = "white",
    bg = "#3CD812",
    width = 35,
    height = 2,
)

lblWindSpeed = tk.Label(
    text = "pH",
    fg = "white",
    bg = "#3CD812",
    width = 35,
    height = 2,
)

lblLightLevel = tk.Label(
    text = "Light Level",
    fg = "white",
    bg = "#3CD812",
    width = 35,
    height = 2,
)

#frame = tk.Frame(master = window, width = 150, height = 150)

#buttons
btnMeasurements = tk.Button(window,
    text="Options",
    command = openOptionsWindow,
    width=15,
    height=2,
    bg="blue",
    fg="yellow"
)

btnPlants = tk.Button(window,
    text="Plants",
    command = openPlantsWindow,
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
)

btnEnvironment = tk.Button(window,
    text="Environment",
    command = openEnvironmentWindow,
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
)

#gauges
cnvTemperature = tk.Canvas(bg ="blue", height = 180, width = 300)
coord = 20, 50, 280, 210
arcAlert = cnvTemperature.create_arc(coord, start = 120, extent = 60, fill = "red")
arcWarning = cnvTemperature.create_arc(coord, start = 90, extent = 30, fill = "yellow")
arcOptimal = cnvTemperature.create_arc(coord, start = 0, extent = 90, fill = "green")

cnvHumidity = tk.Canvas(bg ="blue", height = 180, width = 300)
coord = 20, 50, 280, 210
arc = cnvHumidity.create_arc(coord, start = 0, extent = 150, fill = "red")

cnvWindSpeed = tk.Canvas(bg ="blue", height = 180, width = 300)
coord = 20, 50, 280, 210
arc = cnvWindSpeed.create_arc(coord, start = 0, extent = 150, fill = "red")

cnvLightLevel = tk.Canvas(bg ="blue", height = 180, width = 300)
coord = 20, 50, 280, 210
arc = cnvLightLevel.create_arc(coord, start = 0, extent = 180, fill = "red")

#text example
"""
entry = tk.Entry(fg="yellow, bg="blue", width = 50
"""

#establish window size
window.geometry("1300x425")

#places widgets
lblTitle.grid(row = 0, column = 1, columnspan = 2, pady = 5)

lblTime.grid(row = 0, column = 0, pady = 5)

lblDate.grid(row = 0, column = 3, pady = 5)

lblTemperature.grid(row = 2, column = 0, padx = 5, pady = 5)

lblHumidity.grid(row = 2, column = 1, padx = 5, pady = 5)

lblWindSpeed.grid(row = 2, column = 2, padx = 5, pady = 5)

lblLightLevel.grid(row = 2, column = 3, padx = 5, pady = 5)

btnMeasurements.grid(row = 1, column = 0, columnspan = 2, pady = 10)

btnPlants.grid(row = 1, column = 1, columnspan = 2, pady = 10)

btnEnvironment.grid(row = 1, column = 2, columnspan = 2, pady = 10)

cnvTemperature.grid(row = 3, column = 0, padx = 10, pady = 10)

cnvHumidity.grid(row = 3, column = 1, padx = 10, pady = 10)

cnvWindSpeed.grid(row = 3, column = 2, padx = 10, pady = 10)

cnvLightLevel.grid(row = 3, column = 3, padx = 10, pady = 10)

#entry.pack()

#Program exit
window.mainloop()
