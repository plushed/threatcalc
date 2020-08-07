import argparse
import os.path
import pandas
import plotly.express as px
from tkinter import *
from PIL import ImageTk,Image

VERSION = "0.1"

# Start
# Main Function
def gui():
    main_window = Tk()
    # size of the window
    main_window.geometry('670x480')
    main_window.title("Threat Calculator")
    # Menu Declaration
    menu = Menu(main_window)
    main_window.config(menu=menu)
    # Restart Program Function
    def restart_program():
        python = sys.executable
        os.execl(python, python, *sys.argv)
    menu.add_command(label="Main", command=restart_program)

    # Create Tkinter variables
    oppVar = StringVar(main_window)
    intVar = StringVar(main_window)
    capVar = StringVar(main_window)

    # Define Frames
    contentframe = LabelFrame(main_window, padx=5, pady=5)
    contentframe.grid(column=3, row=0, columnspan=5, rowspan=8, pady=15)
    resultframe = LabelFrame(main_window, padx=5, pady=5)
    resultframe.grid(row=7, column=0, columnspan=2)

    # Calc Function
    def calc():
        # Evaluate Intent
        intresult = 0
        if intVar.get() == "Low":
            intresult = 0
        elif intVar.get() == "Moderate":
            intresult = 1
        elif intVar.get() == "High":
            intresult = 2
        else:
            intresult = 3

        # Evaluate Opportunity
        oppresult = 0
        if oppVar.get() == "Low":
            oppresult = 0
        elif oppVar.get() == "Moderate":
            oppresult = 1
        elif oppVar.get() == "High":
            oppresult = 2
        else:
            oppresult = 3

        # Evaluate Capability
        capresult = 0
        if capVar.get() == "Low":
            capresult = 0
        elif capVar.get() == "Moderate":
            capresult = 1
        elif capVar.get() == "High":
            capresult = 2
        else:
            capresult = 3

        # Evaluate Severity based on criteria
        result = capresult + intresult + oppresult
        if result <= 2:
            severity = "Low"
        elif 2 < result <= 4:
            severity = "Moderate"
        elif 4 < result <= 6:
            severity = "High"
        else:
            severity = "Critical"

        # Evaluate Threat Nature
        if intresult > 1 and oppresult > 1 and capresult > 1:
            theat_type = "Imminent"
        elif intresult > 0 and oppresult > 0 and capresult <= 1:
            theat_type = "Insubstantial"
        elif intresult > 0 and capresult > 1:
            theat_type = "Impending"
        elif intresult == 0 and oppresult > 1 and capresult > 1:
            theat_type = "Potential"
        else:
            theat_type = "Nonexistent"
        final_result = "There is a " + severity + " " + theat_type + " Threat"

        #Output result to frame
        resultframe.config(text=final_result, font=("Helvetica", 9, "bold"))

    # Add image
    img = ImageTk.PhotoImage(Image.open("model.png"))
    Label(contentframe, image=img).grid()

    #row 1
    oppLabel = Label(main_window, text="Opportunity", font=("Helvetica", 12, "bold"), anchor=W, justify=LEFT)
    oppLabel.grid(row=0, column=0)

    # Dictionary with options
    oppchoices = ['Low', 'Moderate', 'High', 'Critical']
    oppVar.set('Low')  # set the default option
    popupMenu = OptionMenu(main_window, oppVar, *oppchoices)
    popupMenu.config(width=20)
    Label(main_window, text="Choose a rating").grid(row=0, column=1, pady=10)
    popupMenu.grid(row=1, column=0, columnspan=2)

    # row 2
    intLabel = Label(main_window, text="Intent", font=("Helvetica", 12, "bold"), anchor=W, justify=LEFT)
    intLabel.grid(row=2, column=0)

    # Dictionary with options
    intchoices = ['Low', 'Moderate', 'High', 'Critical']
    intVar.set('Low')  # set the default option
    popupMenu = OptionMenu(main_window, intVar, *intchoices)
    popupMenu.config(width=20)
    Label(main_window, text="Choose a rating").grid(row=2, column=1, pady=10)
    popupMenu.grid(row=3, column=0, columnspan=2)

    # row 3
    capLabel = Label(main_window, text="Capability", font=("Helvetica", 12, "bold"), anchor=W, justify=LEFT)
    capLabel.grid(row=4, column=0)

    # Dictionary with options
    capchoices = ['Low', 'Moderate', 'High', 'Critical']
    capVar.set('Low')  # set the default option
    popupMenu = OptionMenu(main_window, capVar, *capchoices)
    popupMenu.config(width=20)
    Label(main_window, text="Choose a rating").grid(row=4, column=1,  pady=10)
    popupMenu.grid(row=5, column=0, columnspan=2)

    #submit button
    submitButton = Button(main_window, text="Submit", font=("bold"), width=20, command=calc)
    submitButton.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

    #Display Results
    Label(resultframe).grid(row=7, column=0, columnspan=2)

    main_window.mainloop()

if __name__ == '__main__':
    gui()
