# Image Steganography GUI

## 📌 Project Overview
This project is a **Graphical User Interface (GUI) for Image Steganography** that allows users to securely hide and retrieve text messages within images. The application is built using **Python, OpenCV, and Tkinter**, ensuring a smooth and user-friendly experience.

## 🎯 Features
- **Encode text into images** 📷
- **Decode hidden messages from images** 🔍
- **Simple and intuitive GUI** 🖥️
- **Supports PNG and JPEG formats**
- **Efficient and secure text embedding** 🔐

## 🛠️ Installation
### Prerequisites
Ensure you have Python installed (Recommended: Python 3.7+). You will also need the following dependencies:

```sh
pip install opencv-python numpy pillow
```

## 🚀 How to Run
1. **Clone the repository** (or download the script)
   ```sh
   git clone https://github.com/your-repo/steganography-gui.git
   cd steganography-gui
   ```

2. **Run the script**
   ```sh
   python main.py
   ```

## 📌 Usage Instructions
### Encoding a Message
1. Click **Browse** to select an image.
2. Enter the secret message.
3. Click **Encode** to hide the message in the image.
4. The encoded image is saved as `encoded_image.png`.

### Decoding a Message
1. Click **Browse** to select the encoded image.
2. Click **Decode** to reveal the hidden message.

## ✅ Project Highlights
- **User-friendly**: Simple GUI for easy interaction.
- **Security**: Uses pixel manipulation to hide data securely.
- **Scalability**: Can be extended with encryption for added security.

## 📜 License
This project is open-source and free to use. Contributions are welcome! 🤝

