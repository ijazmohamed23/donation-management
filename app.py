import os

# Vulnerability 1: Hardcoded secret (GK-005)
API_KEY = "sk_live_1234567890abcdef1234567890"

def run_action(cmd):
    # Vulnerability 2: Command injection (GK-002)
    os.system(cmd)
