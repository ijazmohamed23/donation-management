import os
import pickle
import subprocess

# Flaw 1: Hardcoded Secret (GK-005 / CWE-798)
API_KEY = "sk_live_9876543210abcdef9876543210"

def get_user(user_id):
    # Flaw 2: SQL Injection (GK-001 / CWE-89)
    query = "SELECT * FROM users WHERE id=" + user_id
    cursor.execute(query)

def ping_server(host):
    # Flaw 3: Command Injection (GK-002 / CWE-78)
    os.system("ping -c 1 " + host)

def run_calculation(user_code):
    # Flaw 4: Code Injection (GK-003 / CWE-94)
    eval(user_code)

def load_session(data):
    # Flaw 5: Insecure Deserialization (GK-004 / CWE-502)
    pickle.loads(data)
