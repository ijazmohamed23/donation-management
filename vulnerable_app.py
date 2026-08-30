import os
import yaml

# 1. Hardcoded Secret (Gitleaks will catch this)
AWS_SECRET_KEY = os.getenv("AKIAIOSFODNN7EXAMPLE_ENV_VAR", "")

# 2. Insecure YAML Deserialization (Semgrep will catch this)
def load_donation_data(raw_data):
    return yaml.load(raw_data)
