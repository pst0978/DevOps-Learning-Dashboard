import os
import requests

# Default fallback 'pst0978' rakha hai agar GITHUB_USER system me na mile
username = os.getenv('GITHUB_USER', 'pst0978')
url = f"https://api.github.com/users/{username}"

print(f"Fetching data securely for user: {username}...")
print("----------------")

response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    print("SUCCESS: Live data fetched securely.")
    print(f"GITHUB Username: {user_data['login']}")
    print(f"Public Repositories: {user_data['public_repos']}")
else:
    print(f"Alert: Failed to Connect. Status code: {response.status_code}")