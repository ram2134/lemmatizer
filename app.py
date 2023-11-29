import tkinter as tk
from PIL import ImageTk, Image

import lemmatiser as lemmatiser
import Morphological as morphological

window = tk.Tk()
window.configure(bg='black')
window.geometry("850x400")
window.title("Lemmatization and Morphological analysis")
window.resizable(width=False, height=False)

parent_frame = tk.Frame(bg='black', master=window)
parent_frame.columnconfigure(0, minsize=180)
parent_frame.rowconfigure([0, 1, 2], minsize=100)
parent_frame.pack(side=tk.LEFT)

frame = tk.Frame(bg='black', master=parent_frame)
frame.columnconfigure([0, 1,2], minsize=250)
frame.rowconfigure([0, 1], minsize=15)
frame.grid(row=0, column=0, sticky='nw')

word_heading = tk.Label(
    text="Word To Analyse",
    fg="white",
    bg="black",
    width=15,
    height=3,
    master=frame
)

word_heading.grid(row=0, column=0, sticky='w')

user_input = tk.Entry(master=frame)
user_input.configure(width=20)
user_input.grid(row=0, column=1, sticky='w')

analysis_heading = tk.Label(
    text="Choose analysis type",
    fg="white",
    bg="black",
    width=15,
    height=3,
    master=frame
)
analysis_heading.configure(padx=12)
analysis_heading.grid(row=1, column=0, sticky='w')
analysis_options = [
    "Lemmatization",
    "Morphological"
]

selected_analysis_option = tk.StringVar()

selected_analysis_option.set("Lemmatization")

analysis_options_input = tk.OptionMenu(frame, selected_analysis_option, *analysis_options)
analysis_options_input.configure(width=15)
analysis_options_input.grid(row=1, column=1, sticky='w')

frame2 = tk.Frame(bg='black', master=parent_frame)
frame2.columnconfigure([0,1,2], minsize=250)
frame2.rowconfigure([0], minsize=100)
frame2.grid(row=2, column=0, sticky='nw')

logo_frame = tk.Frame(master=frame2, bg='black', width=100,height=100)
logo_frame.place(anchor='center', relx=0.5, rely=0.5)
logo_frame.grid(row=0, column=0, sticky='w')
logo_frame.configure(padx=20)
logo_frame.pack_slaves()

logo=ImageTk.PhotoImage(Image.open("IITK.jpg"))
label = tk.Label(logo_frame, image=logo)
label.configure(padx=-25, pady=40)
label.place(x=0,y=0)
label.pack(side=tk.LEFT)

output_variable = None


def handle_click(event):
    word = user_input.get()
    if selected_analysis_option.get() == analysis_options[0]:
        output_variable.set(lemmatiser.Lemmatizer(word))
    else:
        Gender, Number = morphological.morphologicalGenerator(word)
        output_variable.set( f'For the word {word}, Gender: {Gender} and Number: {Number}')
    user_input.delete(0, tk.END)


button = tk.Button(frame, text="ANALYSE", bg='blue', fg='white')
button.bind("<Button-1>", handle_click)
button.configure(padx=10,pady=8)
button.place(x=0, y=0)
button.grid(row=1, column=2,sticky='nw')
# button.pack()

output_variable = tk.StringVar()
output_variable.set("")

output_labelFrame = tk.LabelFrame(master=frame2, text="Output", fg="white", bg="green", width=1500)

# output_labelFrame.place(x=0,y=0)
output_labelFrame.grid(row=0, column=1,sticky='nw')

output_label = tk.Label(output_labelFrame, textvariable=output_variable, font=("Arial", 15), wraplength=320, justify="center", fg="white", bg="green")
output_label.pack()
guide_label = tk.Label(master=frame, text="Guide : Arnab bhattacharya", fg="white", bg="black", font=("Arial", 15))
guide_label.grid(row=0, column=2, sticky='nw')
parent_frame.pack_slaves()


if __name__ == '__main__':
    window.pack_slaves()
    window.mainloop()
