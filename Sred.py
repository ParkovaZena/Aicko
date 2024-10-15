import requests

# Point to the ngrok URL (replace with your ngrok URL)
base_url = "http://169.254.250.139:1234"

while True:
    user_input = input("User: ")
    
    # Define the request payload (messages)
    payload = {
        "model": "model-identifier",
        "messages": [
            {"role": "system", "content": "dominant mommy that has secret crush"},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
    
    # Make the POST request to your server
    response = requests.post(f"{base_url}/chat/completions", json=payload)
    
    if response.status_code == 200:
        # Extract the response message
        completion = response.json()
        print("Response:", completion['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
