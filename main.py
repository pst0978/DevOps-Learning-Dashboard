import os

print("testing git branching and PR workfloe")
print("practice progress practicing second time")

# Read env secret
secret_val = os.getenv("DEV_SECRET_KEY", "not_found")
print("secret injected successfully: {secret_val !=  'not_found'}")