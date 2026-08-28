import os
import yaml

# 1. Hardcoded Secret (Gitleaks will catch this)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

# 2. Insecure YAML Deserialization (Semgrep will catch this)
def load_donation_data(raw_data):
    return yaml.load(raw_data)
