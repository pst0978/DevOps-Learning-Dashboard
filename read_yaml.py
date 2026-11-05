import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print("--- YAML Config Loaded Successfully ---")
print(f"App Name: {config['app_name']}")
print(f"DB Host: {config['database']['host']}")
print(f"DB Port: {config['database']['port']}")
print(f"First Service: {config['services'][0]}")