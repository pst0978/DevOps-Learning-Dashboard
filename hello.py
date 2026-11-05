import requests
url = "https://api.github.com"
print("connecting to GitHub Server via API....")
print("--------")


response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()

    print("SUCCESS: Live data fetched successfully!")
    print(f"GitHub Username: {user_data['pst09178_repos']}")
    print(f"profile created at: {user_data['created_at']}")

else:  

    print(f"Alert: Failed to connect:Status Code: {response.status_code}") 