import cv2
import numpy as np
from PIL import Image
from Crypto.Cipher import AES
import base64
import os

# AES Encryption Parameters (for Steganography)
SECRET_KEY = b"thisisasecretkey12"  # 16-character key (AES-128)
IV = b"thisisaninitvectr"           # 16-character IV (AES-128)

# -------------------- FILTERING FUNCTIONS --------------------

def apply_filter(input_path, output_path, filter_type):
    try:
        image = cv2.imread(input_path)

        if image is None:
            print("Error: Could not load image.")
            return False

        if filter_type == "grayscale":
            filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif filter_type == "sepia":
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            filtered_image = cv2.transform(image, kernel)
        elif filter_type == "negative":
            filtered_image = cv2.bitwise_not(image)
        elif filter_type == "blur":
            filtered_image = cv2.GaussianBlur(image, (15, 15), 0)
        elif filter_type == "edge":
            filtered_image = cv2.Canny(image, 100, 200)
        elif filter_type == "brightness_contrast":
            alpha = 1.5  # Contrast control (1.0-3.0)
            beta = 30    # Brightness control (0-100)
            filtered_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        else:
            print("Error: Unknown filter type.")
            return False

        cv2.imwrite(output_path, filtered_image)
        return True

    except Exception as e:
        print(f"Error applying filter: {str(e)}")
        return False

# -------------------- STEGANOGRAPHY FUNCTIONS --------------------

# Padding for AES Encryption
def pad_message(message):
    padding_size = 16 - (len(message) % 16)
    return message + (chr(padding_size) * padding_size)

def unpad_message(message):
    return message[:-ord(message[-1])]

# AES Encryption
def encrypt_message(message):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    return base64.b64encode(cipher.encrypt(pad_message(message).encode())).decode()

# AES Decryption
def decrypt_message(encrypted_message):
    try:
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
        return unpad_message(cipher.decrypt(base64.b64decode(encrypted_message)).decode())
    except Exception as e:
        return f"[ERROR] Decryption Failed: {str(e)}"

# Hide Message in Image
def hide_message(image_path, message):
    encrypted_msg = encrypt_message(message)
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    binary_msg = ''.join(format(ord(char), '08b') for char in encrypted_msg)
    
    index = 0
    for y in range(img.height):
        for x in range(img.width):
            if index < len(binary_msg):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_msg[index])
                pixels[x, y] = (r, g, b)
                index += 1
    
    hidden_img_path = image_path.replace("uploads", "filtered")
    img.save(hidden_img_path)
    return hidden_img_path  # Return the new image path

# Extract Message from Image
def extract_message(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    binary_msg = ""

    for y in range(img.height):
        for x in range(img.width):
            binary_msg += str(pixels[x, y][0] & 1)

    byte_array = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    extracted_msg = ''.join(chr(int(byte, 2)) for byte in byte_array if 32 <= int(byte, 2) <= 126)
    
    return decrypt_message(extracted_msg)  # Decrypt and return the message

