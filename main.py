import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

img = None

# Load image
def load_image():
    global img, panel
    path = filedialog.askopenfilename()
    if path:
        img = cv2.imread(path)
        show_image(img)

# Display image
def show_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = image.resize((400, 400))
    imgtk = ImageTk.PhotoImage(image=image)
    panel.config(image=imgtk)
    panel.image = imgtk

# Grayscale
def grayscale():
    global img
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

# Blur
def blur():
    global img
    if img is not None:
        blurred = cv2.GaussianBlur(img, (15, 15), 0)
        show_image(blurred)

# Edge Detection
def edge():
    global img
    if img is not None:
        edges = cv2.Canny(img, 100, 200)
        show_image(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

# Save image
def save_image():
    global img
    if img is not None:
        path = filedialog.asksaveasfilename(defaultextension=".jpg")
        cv2.imwrite(path, img)

# GUI
root = Tk()
root.title("Image Editor App")

panel = Label(root)
panel.pack()

btn_frame = Frame(root)
btn_frame.pack()

Button(btn_frame, text="Load Image", command=load_image).grid(row=0, column=0)
Button(btn_frame, text="Grayscale", command=grayscale).grid(row=0, column=1)
Button(btn_frame, text="Blur", command=blur).grid(row=0, column=2)
Button(btn_frame, text="Edge", command=edge).grid(row=0, column=3)
Button(btn_frame, text="Save", command=save_image).grid(row=0, column=4)

root.mainloop()