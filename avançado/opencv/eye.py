import cv2
import tkinter as tk
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        # Converte para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)
    lbl.after(10, update_frame)

root = tk.Tk()
lbl = tk.Label(root)
lbl.pack()

update_frame()
root.mainloop()

cap.release()
