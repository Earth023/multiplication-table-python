import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='It is all Zeroo.')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(i * number) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title("Multiplication Table ")
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text="Multiplication Table ")
title_label.pack(pady=10)

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(
    master=window, text="Go",
    command=show_output, width=10, height=1, bg="red", fg="white"
)
go_button.pack(pady=5)

output_label = tk.Label(master=window)
output_label.pack(pady=10)

window.mainloop()
