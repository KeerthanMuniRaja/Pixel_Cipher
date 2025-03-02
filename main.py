import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function to encode text into an image
def encode_text(image_path, text, output_path):
    img = cv2.imread(image_path)
    text += "####"  # Delimiter to identify the end of the message
    binary_text = ''.join(format(ord(i), '08b') for i in text)
    
    data_index = 0
    binary_text_len = len(binary_text)
    rows, cols, channels = img.shape
    
    for row in range(rows):
        for col in range(cols):
            for channel in range(channels):
                if data_index < binary_text_len:
                    img[row, col, channel] = (img[row, col, channel] & 254) | int(binary_text[data_index])
                    data_index += 1
                else:
                    break
    
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", "Message encoded successfully!")

def decode_text(image_path):
    img = cv2.imread(image_path)
    binary_text = ""
    
    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_text += str(channel & 1)
    
    text = "".join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
    text = text.split("####")[0]  # Extract message before delimiter
    
    messagebox.showinfo("Decoded Message", f"Hidden message: {text}")

# GUI Application
def browse_image(entry):
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def encode_gui():
    image_path = img_entry.get()
    message = text_entry.get("1.0", tk.END).strip()
    if not image_path or not message:
        messagebox.showerror("Error", "Please select an image and enter a message!")
        return
    
    output_path = "encoded_image.png"
    encode_text(image_path, message, output_path)

def decode_gui():
    image_path = img_entry.get()
    if not image_path:
        messagebox.showerror("Error", "Please select an image!")
        return
    decode_text(image_path)

# Initialize GUI app
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x300")

# Image Selection
tk.Label(root, text="Select Image:").pack()
img_entry = tk.Entry(root, width=40)
img_entry.pack()
tk.Button(root, text="Browse", command=lambda: browse_image(img_entry)).pack()

# Message Input
tk.Label(root, text="Enter Message:").pack()
text_entry = tk.Text(root, height=4, width=40)
text_entry.pack()

# Buttons
tk.Button(root, text="Encode", command=encode_gui).pack()
tk.Button(root, text="Decode", command=decode_gui).pack()

# Run GUI
root.mainloop()
