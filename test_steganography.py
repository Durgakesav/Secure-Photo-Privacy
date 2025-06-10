import requests

# Test hiding message
url = "http://127.0.0.1:5000/hide_message"
file_path = "./faces.jpg"  # Ensure face.jpg exists
message = "This is a secret!"

files = {'file': open(file_path, 'rb')}
data = {'message': message}
response = requests.post(url, files=files, data=data)

# Print raw response before converting to JSON
print("Raw Response:", response.text)

try:
    print("Hiding Message Response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Error: Server did not return a valid JSON response.")

# Test extracting message
url = "http://127.0.0.1:5000/extract_message"
files = {'file': open(file_path, 'rb')}
response = requests.post(url, files=files)

# Print raw response before converting to JSON
print("Raw Response:", response.text)

try:
    print("Extracted Message:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Error: Server did not return a valid JSON response.")
