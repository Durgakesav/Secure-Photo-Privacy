from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

# AES Configuration
SECRET_KEY = b"this_is_a_32_byte_secret_key_123"  # 32 bytes key
IV = b"initialization_v"                          # 16 bytes IV

# ✅ Encrypt a message using AES
def encrypt_message(message):
    try:
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
        padded_message = pad(message.encode('utf-8'), AES.block_size)
        encrypted = cipher.encrypt(padded_message)
        return encrypted
    except Exception as e:
        print(f"[Encryption Error] {str(e)}")
        return None

# ✅ Decrypt a message using AES
def decrypt_message(encrypted_bytes):
    try:
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
        decrypted = cipher.decrypt(encrypted_bytes)
        unpadded = unpad(decrypted, AES.block_size)
        return unpadded.decode('utf-8')
    except Exception as e:
        return f"[Decryption Error] {str(e)}"

# ✅ Hide message inside image using LSB steganography
def hide_message(image_filename, message):
    try:
        encrypted_data = encrypt_message(message)
        if encrypted_data is None:
            return None

        # Load image
        img_path = os.path.join("static", "uploads", image_filename)
        img = Image.open(img_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        # Convert encrypted data to binary
        binary_data = ''.join(format(byte, '08b') for byte in encrypted_data)

        # Add start and end markers
        start_marker = '1111111111111111'
        end_marker = '1111111111111110'
        binary_message = start_marker + binary_data + end_marker

        # Check if message fits in image
        if len(binary_message) > width * height * 3:
            return None  # Message too large

        # Hide bits into LSBs of image pixels
        idx = 0
        for y in range(height):
            for x in range(width):
                if idx >= len(binary_message):
                    break
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[idx]) if idx < len(binary_message) else r
                idx += 1
                g = (g & ~1) | int(binary_message[idx]) if idx < len(binary_message) else g
                idx += 1
                b = (b & ~1) | int(binary_message[idx]) if idx < len(binary_message) else b
                idx += 1
                pixels[x, y] = (r, g, b)

        # Save the stego image
        stego_path = os.path.join("static", "filtered", f"stego_{image_filename}")
        img.save(stego_path, "PNG")
        return stego_path

    except Exception as e:
        print(f"[Hiding Error] {str(e)}")
        return None

# ✅ Extract message from image using LSB steganography
def extract_message(image_filename):
    try:
        img_path = os.path.join("static", "filtered", image_filename)
        img = Image.open(img_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        bits = ""
        start_marker = '1111111111111111'
        end_marker = '1111111111111110'

        # Extract all LSBs
        for y in range(height):
            for x in range(width):
                for channel in pixels[x, y]:
                    bits += str(channel & 1)

        # Find markers
        start_index = bits.find(start_marker)
        if start_index == -1:
            return "[ERROR] Start marker not found"
        start_index += len(start_marker)

        end_index = bits.find(end_marker, start_index)
        if end_index == -1:
            return "[ERROR] End marker not found"

        message_bits = bits[start_index:end_index]

        # Convert bits to bytes
        byte_array = bytearray()
        for i in range(0, len(message_bits), 8):
            byte = message_bits[i:i+8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))

        # Decrypt the message
        decrypted = decrypt_message(bytes(byte_array))
        return decrypted

    except Exception as e:
        return f"[ERROR] Failed to extract message: {str(e)}"
