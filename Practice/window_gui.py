#Python 2.7.10
import Tkinter

window = Tkinter.Tk()
window.title("Muddassir")
window.geometry("300x300")
#We can set an icon in the window titlebut it must be bitmap
#window.wm_iconbitmap('file.ico')
#Adding labels and buttons
label = Tkinter.Label(window, text="Label")
entry = Tkinter.Entry(window)
bttn = Tkinter.Button(window, text="Button")
#Packing it in the window
label.pack()
entry.pack()
bttn.pack()
#Draw the window
window.mainloop()
