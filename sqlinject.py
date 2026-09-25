import os
import sqlite3
import yaml

# 1. Hardcoded Secret (Gitleaks Secret Engine will flag)
AWS_SECRET_KEY = os.getenv("AKIAIOSFODNN7EXAMPLE_ENV_VAR", "")

# 2. Dynamic SQL Injection (Trained ML Engine will detect this dynamic query!)
def get_donor_by_username(user_input_name):
    conn = sqlite3.connect("donations.db")
    cursor = conn.cursor()
    
    # ❌ VULNERABLE: String formatted dynamic query allows ' OR '1'='1 SQL injection
    query = "SELECT donor_name, total_donations FROM donors WHERE username = '%s'" % user_input_name
    cursor.execute(query)
    return cursor.fetchall()

# 3. Unsafe Deserialization (Semgrep SAST will flag)
def load_donor_backup(backup_yaml):
    return yaml.safe_load(backup_yaml)
