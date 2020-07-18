from PIL import ImageTk, Image
import PySimpleGUI as sg


def get_unknown_game_name(file):
    sg.theme("DarkAmber")


    # Loading the image into a format that Tkinter can use
    image = Image.open(file)
    image.save(".temp", "png")
    # filepath = str(file)
    image = open(file, "rb")

    LAYOUT = [
        [sg.Image(data=image.read())],
        [sg.Text("Name of image:"), sg.InputText()],
        [sg.Button("Confirm"), sg.Button("Cancel")]
    ]


    window = sg.Window(
        "Unknown Image",
        LAYOUT,
        keep_on_top=True,
        resizable=True
    )


    # Listen for events
    while True:

        event, values = window.read()

        # Closing the window, set game to unknown
        if event in (None, "Cancel"):
            window.close()
            return "Unknown"

        # Setting the game name appropriately
        if event in ("Confirm"):
            window.close()
            return values[0]