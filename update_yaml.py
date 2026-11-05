import yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(f"purana version: {config['version']}")
config['version'] = '1.1.0' 
config['database']['[port]'] = 4312

with open('config.yaml', 'w' ) as file:
    yaml.dump(config, file, default_flow_style=False)

print("---YAML File Successfully Updated and saved")