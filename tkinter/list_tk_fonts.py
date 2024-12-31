# list_tk_fonts.py
# Rajdeep Sandhu
# Python version: 3.12.5

# List all available fonts in Tk. Copy font name to clipboard when clicked.
# Derived from:
# https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
# (by https://stackoverflow.com/users/10050244/jimmiesrustled)

from tkinter import *
from tkinter import font


def populate(frame: Frame) -> None:
    """Add fonts to the frame"""
    listnumber = 1

    for item in fonts:
        label = "listlabel" + str(listnumber)
        label = Label(frame, text=item, font=(item, 16))

        # Copy font name to clipboard when clicked
        label.bind("<Button-1>", lambda e, text=item: copy_to_clipboard(text))

        label.pack()
        listnumber += 1


def onFrameConfigure(canvas: Canvas) -> None:
    """Reset the scroll region to encompass the inner frame"""
    canvas.configure(scrollregion=canvas.bbox("all"))


def copy_to_clipboard(text: str) -> None:
    """
    Copy text to clipboard

    Args:
    :param text: Text to copy to clipboard
    """

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


if __name__ == "__main__":
    # Set up root window
    root = Tk()
    root.title("Font Families")

    # Get list of fonts
    fonts = list(font.families())
    fonts.sort()

    # Setup UI
    canvas = Canvas(root, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame)

    root.mainloop()
