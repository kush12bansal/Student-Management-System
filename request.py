import requests
from datetime import datetime

url = 'http://127.0.0.1:5000/api/students'  # Correct endpoint for adding a student

students = [
    {
        "first_name": "ABC",
        "last_name": "XYZ",
        "email": "abc@gmail.com",
        "enrollment_date": datetime.now().strftime('%Y-%m-%d')  # Add enrollment date
    },
    {
        "first_name": "DEF",
        "last_name": "GHI",
        "email": "def@gmail.com",
        "enrollment_date": datetime.now().strftime('%Y-%m-%d')  # Add enrollment date
    }
]
for student in students:
    response = requests.post(url, json=student)
    print(response.json())  # Print the response from the server
