from steganography import extract_message

image_filename = "stego_Screenshot 2025-02-23 133445.png"
image_path = f"static/filtered/{image_filename}"

extracted_msg = extract_message(image_path)

print("Extracted Message:", extracted_msg)
