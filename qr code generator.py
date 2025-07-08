import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter some data to generate QR Code.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')  # Convert for Tkinter compatibility

    # Save and display QR Code
    img.save("qr.png")

    # Resize for display
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep reference!

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.config(padx=20, pady=20)

tk.Label(root, text="Enter text or URL:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12)).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
