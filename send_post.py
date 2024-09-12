import requests

# Define the URL and the data
url = 'https://wyyi0kpjpf.execute-api.us-east-1.amazonaws.com/'
data = {
    'receiver_email': 'tanmayrastogi57@gmail.com',
    'subject': 'Hello',
    'body': 'This is a test email.'
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
